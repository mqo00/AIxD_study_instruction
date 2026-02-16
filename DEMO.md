# Demo Instructions

This page explains how to try the **Tetris** (game) and **ProofReader** (chatbot) tasks. On the study day, you will follow similar steps with the corresponding tasks.

---

## General Task Steps

1. **Open the right folder in VS Code**  
   In VS Code, go to **File → Open Folder** and choose the folder for your task (e.g. `AIxD_study_instruction/tetris` or `AIxD_study_instruction/proofreader`).  
   [How to open a folder in VS Code](https://code.visualstudio.com/docs/getstarted/getting-started#_open-a-folder-in-vs-code)

2. **Turn on the Archiver**  
   When asked to enable “Copilot Interaction Archiver” for this workspace, click **Yes**.

3. **Open GitHub Copilot Chat**  
   In the menu, click **View → GitHub Copilot Chat**, or click the Copilot icon in the sidebar.  
   [About GitHub Copilot Chat](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=visualstudio#ask-questions-in-the-chat-window)

4. **Do the task**  
   Your task here is to interact with the **Copilot** coding agent to implement the provided app (e.g., Tetris) in VSCode. Your goal is to **write a prompt** that is sufficient to **reproduce** key functionalities and features in this app as closely as possible. You can prompt the coding agent however you like, but **only in text (no screenshots)**. 

5. **Save a snapshot when you’re done**  
   - Click the **“Archiver: {yourid}”** button at the bottom right of VS Code, then **“Capture Repo Snapshot”**,  
   - Or use the Command Palette: type **“Copilot Archiver: Capture Now”** and run that command.

---

## Game Task Demo

1. **Open the Tetris folder**  
   In VS Code, open the folder: **AIxD_study_instruction/tetris`** and open Copilot (as in the general steps 1-3 above).

2. **Prompt Copilot to build the game**  
   In GitHub Copilot Chat, type a prompt in plain English, for example:  
   *“Implement a simple Tetris game in Python in the file tetris.py.”*  

3. **Run the game**  
   Open the [Terminal](#frequent-commands) in VS Code (View → Terminal).

   Enter command to run `python tetris.py`  
   (If Copilot implements in different languages, you may need to use different commands such as npm run dev for react apps.)

4. **Play the game**  
   Depending on how the game was built, open the game in your browser by clicking URL or use **Simple Browser** via the [Command Palette](#frequent-commands) (View → Command Palette): “Simple Browser: Show” → enter the URL.

5. **Keep working on the task**  
   Try to enter another prompt to make your game closer to this [reference Tetris game](https://academy.cs.cmu.edu/sharing/dodgerBlueSpider7058).

6. **Save a snapshot of your workspace** (as in the general step 5 above).
---

## Chatbot Task Demo


1. **Open the ProofReader folder**  
   In VS Code, open the folder: **AIxD_study_instruction/proofreader** and open Copilot (as in the general steps 1-3 above).

2. **Start the chatbot**  
   Open the [Terminal](#frequent-commands) in VS Code (View → Terminal).

   In the terminal, navigate to the chatbot folder `cd ../chatbot`
   
   Run Python (For the first time, it will install some packages): 
   ```bash
   python -m pip install -r requirements.txt && python chatbot.py
   ```  
   Later (such as on the study date), you can simply run:  
   `python ../chatbot/chatbot.py` from the task folder (e.g., tripadvisor)

3. **Open the chatbot in Simple Browser**  
   [Command Palette](#frequent-commands) (View → Command Palette): “Simple Browser: Show” → paste http://127.0.0.1:5000 and press Enter.

4. **Choose “Proof Reader”**  
   On the chatbot page, pick **“Proof Reader”**. Type **“what can you do”** and send.
    **Note:** The chatbot needs an API key to work. Copy paste the key in `chatbot/.env` (see [SETUP.md](SETUP.md#4-configure-the-chatbot-for-iterative-chatbot-tasks)).

5. **Change how Proof Reader behaves**  
   - In the left file list, open **`proofreader/proofreader_prompt.md`** and type your prompt, for example: *“You are a proof reader.”*  
   You can also work with Copilot to build the prompt, e.g., in **GitHub Copilot Chat**, type a prompt in plain English, for example:  
   *“Write prompt for a proof reader.”*  
    **Note:** You do not need to modify the UI/UX for the chatbot, only work on proofreader_prompt.md.
   - Save the proofreader_prompt.md file: **Cmd+S** (Mac) or **Ctrl+S** (Windows).

6. **Test prompt changes' influence over chatbot**  
   In the chatbot, type **“what can you do”** again and send. The Proof Reader's response should reflect the updated prompt. The other chatbots (e.g. TripAdvisor) will not, because they use the prompt.md file in their corresponding folder.

7. **Keep working on the task**  
   Try to enter another prompt to make your chatbot app closer to the examples provided (Refer to the ProofReader-E1.png & E2.png in the left file list)

8. **Save a snapshot of your workspace** (as in the general step 5 above).




---

## Frequent commands

Use these when the steps say “open Command Palette,” “open the Terminal,” or “open in browser”, etc.

| What you want to do | How to do it |
|---------------------|--------------|
| **Open Command Palette** (run any action by name) | • **Shortcut:** Cmd+Shift+P (Mac) / Ctrl+Shift+P (Windows)<br>• **Menu:** View → Command Palette<br>Then type a few letters (e.g. “terminal”, “simple browser”) and pick the command. |
| **Open the Terminal** | • **Menu:** View → Terminal<br>• **Shortcut:** ⌃` (Control + backtick)<br>• **UI:** Drag a terminal panel up from the bottom of the VS Code window<br>[More on terminal](https://code.visualstudio.com/docs/terminal/getting-started#_run-your-first-command-in-the-terminal) |
| **Navigate in terminal** (change folder) | • `cd folder_name` Terminal starts in your project folder. <br>• `cd chatbot` to enter the chatbot folder from AIxD_study_instruction <br>• `cd ..` — go up one folder|
| **Run a Python script** | From the folder that contains the script: `python script_name.py`<br>• `python chatbot.py` — from the chatbot folder<br>• `python ../chatbot/chatbot.py` — from the proofreader folder |
| **Open a link — Simple Browser** (inside VS Code) | • Open the Command Palette and run **“Simple Browser: Show”**<br>• Paste or type the URL (e.g. `http://127.0.0.1:5000`) and press Enter |
| **Open a link — external browser** (e.g. Chrome) | • In the terminal, when you see a URL like `http://127.0.0.1:5000`, hold **Cmd** (Mac) or **Ctrl** (Windows) and click the link | 
