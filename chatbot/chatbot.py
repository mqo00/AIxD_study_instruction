#!/usr/bin/env python3
"""
Simple chatbot with Outline Assistant or TripAdvisor modes.
Run: pip install -r requirements.txt && python chatbot.py
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from openai import OpenAI

# Load API key from .env
load_dotenv()

# Resolve paths relative to project root (parent of chatbot/)
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTLINE_PROMPT_PATH = PROJECT_ROOT / "outlineassistant" / "prompt.md"
TRIPADVISOR_PROMPT_PATH = PROJECT_ROOT / "tripadvisor" / "prompt.md"

MODE_PROMPTS = {
    "Outline Assistant": OUTLINE_PROMPT_PATH,
    "TripAdvisor": TRIPADVISOR_PROMPT_PATH,
}

app = Flask(__name__)


def load_system_prompt(mode: str) -> str:
    """Load the system prompt from the corresponding prompt.md file."""
    path = MODE_PROMPTS.get(mode, OUTLINE_PROMPT_PATH)
    if path.exists():
        return path.read_text(encoding="utf-8").strip()
    return ""


@app.route("/")
def index():
    return HTML


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    history = data.get("history", [])
    mode = data.get("mode", "Outline Assistant")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or api_key == "enter-your-openai-api-key-here":
        return jsonify({"error": "Please add your OpenAI API key to chatbot/.env (copy from .env.example)."}), 400

    system_prompt = load_system_prompt(mode)

    client = OpenAI(api_key=api_key)

    messages = [{"role": "system", "content": system_prompt or "You are a helpful assistant."}]
    for msg in history:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        content = response.choices[0].message.content or ""
        return jsonify({"content": content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AI Chatbot</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    * { box-sizing: border-box; }
    body { font-family: system-ui, sans-serif; margin: 0; padding: 0; height: 100vh; display: flex; }
    .sidebar {
      width: 220px; border-right: 1px solid #ddd; padding: 1rem; display: flex; flex-direction: column;
      background: #f9f9f9;
    }
    .sidebar h2 { margin: 0 0 0.5rem 0; font-size: 1rem; }
    .mode-buttons { display: flex; flex-direction: column; gap: 0.25rem; margin-bottom: 1rem; }
    .mode-buttons button {
      padding: 0.5rem; font-size: 0.9rem; cursor: pointer; border: 2px solid #ccc;
      background: #fff; border-radius: 6px; text-align: left;
    }
    .mode-buttons button.active { border-color: #0066cc; background: #e6f2ff; }
    #newChat { margin-bottom: 1rem; padding: 0.5rem; background: #0066cc; color: white; border: none; border-radius: 6px; cursor: pointer; }
    #chatList { flex: 1; overflow-y: auto; }
    .chat-item {
      padding: 0.5rem; margin-bottom: 0.25rem; border-radius: 6px; cursor: pointer;
      font-size: 0.85rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }
    .chat-item:hover { background: #eee; }
    .chat-item.active { background: #e6f2ff; }
    .main { flex: 1; display: flex; flex-direction: column; min-width: 0; padding: 1rem; }
    .main h1 { margin: 0 0 0.5rem 0; font-size: 1.25rem; }
    #chat {
      flex: 1; border: 1px solid #ddd; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;
      overflow-y: auto; min-height: 200px; max-height: none;
    }
    .msg { margin-bottom: 1rem; }
    .msg.user { color: #0066cc; }
    .msg.assistant { color: #333; }
    .msg.assistant .content { line-height: 1.5; }
    .msg.assistant .content pre { background: #f5f5f5; padding: 1rem; border-radius: 6px; overflow-x: auto; }
    .msg.assistant .content code { background: #f5f5f5; padding: 0.2em 0.4em; border-radius: 4px; font-size: 0.9em; }
    .msg.assistant .content pre code { background: none; padding: 0; }
    .msg.assistant .content ul, .msg.assistant .content ol { margin: 0.5rem 0; padding-left: 1.5rem; }
    .msg.assistant .content blockquote { border-left: 4px solid #ccc; margin: 0.5rem 0; padding-left: 1rem; color: #666; }
    .msg.assistant .content p { margin: 0.5rem 0; }
    .msg.assistant .content h1, .msg.assistant .content h2, .msg.assistant .content h3 { margin: 1rem 0 0.5rem 0; }
    .input-row { display: flex; gap: 0.5rem; }
    #input { flex: 1; padding: 0.5rem; font-size: 1rem; border-radius: 6px; border: 1px solid #ccc; }
    #send { padding: 0.5rem 1rem; font-size: 1rem; cursor: pointer; background: #0066cc; color: white; border: none; border-radius: 6px; }
    #send:disabled { background: #ccc; cursor: not-allowed; }
    .error { color: #c00; }
    .empty-chat { color: #999; text-align: center; padding: 2rem; }
  </style>
</head>
<body>
  <div class="sidebar">
    <h2>Mode</h2>
    <div class="mode-buttons">
      <button data-mode="Outline Assistant" class="active">Outline Assistant</button>
      <button data-mode="TripAdvisor">TripAdvisor</button>
    </div>
    <button id="newChat">+ New chat</button>
    <h2>Chats</h2>
    <div id="chatList"></div>
  </div>
  <div class="main">
    <h1 id="chatTitle">New chat</h1>
    <div id="chat"></div>
    <div class="input-row">
      <input id="input" type="text" placeholder="Type your message..." autocomplete="off">
      <button id="send">Send</button>
    </div>
  </div>
  <script>
    const STORAGE_KEY = "chatbot_chats";
    let mode = "Outline Assistant";
    let chats = [];
    let currentChatId = null;

    function uuid() { return "c-" + Date.now() + "-" + Math.random().toString(36).slice(2, 11); }

    function loadChats() {
      try {
        const s = localStorage.getItem(STORAGE_KEY);
        chats = s ? JSON.parse(s) : [];
      } catch (e) { chats = []; }
    }

    function saveChats() {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(chats));
    }

    function getChatsForMode() {
      return chats.filter(c => c.mode === mode).sort((a, b) => (b.updatedAt || b.createdAt) - (a.updatedAt || a.createdAt));
    }

    function getCurrentChat() {
      return chats.find(c => c.id === currentChatId);
    }

    function createChat() {
      const chat = { id: uuid(), mode, messages: [], createdAt: Date.now(), updatedAt: Date.now() };
      chats.push(chat);
      saveChats();
      currentChatId = chat.id;
      renderChatList();
      renderChat();
    }

    function selectChat(id) {
      currentChatId = id;
      renderChatList();
      renderChat();
    }

    function renderChatList() {
      const list = document.getElementById("chatList");
      const modeChats = getChatsForMode();
      if (modeChats.length === 0) {
        list.innerHTML = "<div class='empty-chat' style='font-size:0.85rem'>No chats yet</div>";
        return;
      }
      list.innerHTML = modeChats.map(c => {
        const title = c.messages.length ? (c.messages[0].content?.slice(0, 30) || "New chat") + "..." : "New chat";
        return `<div class="chat-item ${c.id === currentChatId ? "active" : ""}" data-id="${c.id}">${escapeHtml(title)}</div>`;
      }).join("");
      list.querySelectorAll(".chat-item").forEach(el => {
        el.onclick = () => selectChat(el.dataset.id);
      });
    }

    function escapeHtml(s) {
      const div = document.createElement("div");
      div.textContent = s;
      return div.innerHTML;
    }

    function renderChat() {
      const container = document.getElementById("chat");
      const chat = getCurrentChat();
      document.getElementById("chatTitle").textContent = chat ? (chat.messages.length ? "Chat" : "New chat") : "New chat";
      if (!chat || chat.messages.length === 0) {
        container.innerHTML = "<div class='empty-chat'>Start a conversation</div>";
        return;
      }
      container.innerHTML = chat.messages.map(m => {
        const div = document.createElement("div");
        div.className = "msg " + m.role;
        if (m.role === "user") {
          div.innerHTML = "<strong>You:</strong> " + escapeHtml(m.content);
        } else {
          const md = (window.marked && (marked.parse || marked)) ? (marked.parse || marked)(m.content) : escapeHtml(m.content);
          div.innerHTML = "<strong>Assistant:</strong> <span class='content'>" + md + "</span>";
        }
        return div.outerHTML;
      }).join("");
      container.scrollTop = container.scrollHeight;
    }

    document.querySelectorAll(".mode-buttons button").forEach(btn => {
      btn.onclick = () => {
        document.querySelectorAll(".mode-buttons button").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        mode = btn.dataset.mode;
        const modeChats = getChatsForMode();
        currentChatId = modeChats.length ? modeChats[0].id : null;
        if (!currentChatId) createChat();
        else { renderChatList(); renderChat(); }
      };
    });

    document.getElementById("newChat").onclick = () => createChat();

    document.getElementById("send").onclick = async () => {
      const input = document.getElementById("input");
      const sendBtn = document.getElementById("send");
      const msg = input.value.trim();
      if (!msg) return;

      if (!currentChatId || !getCurrentChat()) createChat();
      const chat = getCurrentChat();

      input.value = "";
      chat.messages.push({ role: "user", content: msg });
      chat.updatedAt = Date.now();
      saveChats();
      renderChat();
      sendBtn.disabled = true;

      try {
        const res = await fetch("/api/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: msg, history: chat.messages.slice(0, -1), mode })
        });
        const data = await res.json();

        if (!res.ok) {
          chat.messages.push({ role: "assistant", content: "Error: " + (data.error || res.statusText) });
        } else {
          chat.messages.push({ role: "assistant", content: data.content });
        }
        chat.updatedAt = Date.now();
        saveChats();
        renderChat();
      } catch (e) {
        chat.messages.push({ role: "assistant", content: "Error: " + e.message });
        saveChats();
        renderChat();
      }
      sendBtn.disabled = false;
    };

    document.getElementById("input").onkeydown = (e) => {
      if (e.key === "Enter") document.getElementById("send").click();
    };

    loadChats();
    const modeChats = getChatsForMode();
    if (modeChats.length) { currentChatId = modeChats[0].id; }
    else { createChat(); }
    renderChatList();
    renderChat();
  </script>
</body>
</html>
"""


def main():
    print("Starting chatbot at http://127.0.0.1:5000")
    print("Press Ctrl+C to stop.")
    app.run(host="127.0.0.1", port=5000, debug=False)


if __name__ == "__main__":
    main()
