# Study Setup

## 1. Prepare your environment

Before starting, ensure all required extensions are installed and environments are prepared


| Requirement | Details |
|-------------|---------|
| **Python** | Python 3.8 or later. Required to run the chatbot. |
| **VS Code** | [Visual Studio Code](https://code.visualstudio.com/) installed, up-to-date (≥ 1.108). See [VS Code](https://code.visualstudio.com/docs/getstarted/getting-started) tutorials if you haven't used it before.|
| **GitHub account** | A GitHub account (e.g. for cloning the repo and Copilot). |
| **GitHub Copilot** VS Code extensions and **Copilot Pro access** | Install [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) and [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) from VSCode Marketplace. Use your .edu email for [free Copilot Pro access](https://docs.github.com/en/copilot/how-tos/manage-your-account/get-free-access-to-copilot-pro). Note that **student verification may take some days** so start it early. Make sure you are able to prompt the GitHub Copilot Chat coding agent. See [GitHub Copilot Chat](https://code.visualstudio.com/docs/copilot/getting-started#_step-2-build-complete-features-with-agents) tutorials if you haven't used it before. |
| <mark>**Copilot Interaction Archiver** VS Code extension</mark> |  Install the [Copilot Interaction Archiver](https://marketplace.visualstudio.com/items?itemName=Copilot-Archiver.copilot-archiver) (used for data collection in this study). Set up the demo (detailed instructions below): [copilot_archiver_instructions.mov](https://drive.google.com/file/d/18tCphUyFp4M1Gzj-G31jVM62Y9F_9vY2/view?usp=sharing)|

 
## 2. Clone the repository

**[Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository** by entering this command in a terminal window of a folder on your computer, e.g., Desktop or your class folder.

```bash
git clone https://github.com/mqo00/AIxD_study_instruction.git
```

The specific folders in this repository will be your workspace for the corresponding iterative tasks.


## 3. Setup Copilot Interaction Archiver and test Copilot

### Detailed instruction for Copilot Interaction Archiver

Ensure [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot), [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat), and [Copilot Interaction Archiver](https://marketplace.visualstudio.com/items?itemName=Copilot-Archiver.copilot-archiver) are all installed as VS Code extensions.

1. **Log in Copilot Interaction Archiver**

- When prompted, enter your Andrew ID (we only store a hashed ID). Password: `CMU_2026!`
- If the pop-up login fails, press **Cmd+Shift+P** (Mac) or **Ctrl+Shift+P** (Windows), open the Command Palette, and run: **Copilot Archiver: Login**.

2. **Enable workspace**

- When you open a new workspace folder, the extension will ask to enable workspace access. Select `Yes` **only** for your study/homework project.

- If you see “GitHub Copilot Chat must be in Debug mode”, click `Cancel`



### Test run the extensions and Copilot:

 - Select the `AIxD_study_instruction/prep` folder to [open as your workspace](https://code.visualstudio.com/docs/getstarted/getting-started#_open-a-folder-in-vs-code) in VS Code
 - Click `Yes` to Enable Copilot Interaction Archiver for this workspace.
 - Open [GitHub Copilot Chat](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=visualstudio#ask-questions-in-the-chat-window) coding agent by selecting `View` > `GitHub Copilot Chat` or clicking the Copilot icon inside VS Code.
 - Enter a prompt to make sure the coding agent works by implementing a helloworld app in `prep/helloworld.py`. E.g., prompt "make a hello world app", and ask Copilot for how to view the app.
 - When you finish the implementation, take a snapshot of your workspace in VS Code by clicking "Archiver: {yourid}" button (bottom right corner) and "Capture Repo Snapshot" 
    - Or, press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows) to open the Command Palette. Type and run: `Copilot Archiver: Capture Now`.


On the actual study date, the procedural will be similar (you will open the corresponding task folders, e.g., `AIxD_study_instruction/tictactoe` when instructed).



## 4. Configure the chatbot for iterative chatbot tasks

**Create your `.env` file**
   - Rename `chatbot/.env.example` to `chatbot/.env`.
   - Open `chatbot/.env` in a text editor and set your OpenAI API key (enter your own key first, the researcher will provide a new key on the study date):

   ```
   OPENAI_API_KEY=your-openai-api-key-here
   ```

### Test run the chatbot

- Select the `AIxD_study_instruction/outlineassistant` folder to [open as your workspace](https://code.visualstudio.com/docs/getstarted/getting-started#_open-a-folder-in-vs-code) in VS Code.

- Open the [terminal](https://code.visualstudio.com/docs/terminal/getting-started#_run-your-first-command-in-the-terminal) inside VSCode by selecting `View` > `Terminal` from the menu bar, or by pressing the ⌃` keyboard shortcut, or by dragging a terminal window up from the botton of VSCode interface.
    
- Inside the terminal of the outlineassistant folder, enter
    ```bash
    cd ../chatbot
    python -m pip install -r requirements.txt && python chatbot.py
    ```
    After the initial pip installation, you may also directly enter `python ../chatbot/chatbot.py`

- Follow link (cmd + click) to open the chatbot in browser window at http://127.0.0.1:5000.
    Or 
    - Open the Command Palette: Press Ctrl+Shift+P (Windows/Linux) or Cmd+Shift+P (macOS).
    - Run the Command: Type "Simple Browser" and select `Simple Browser: Show` from the list.
    - Enter a URL: An input box will appear, enter http://127.0.0.1:5000
    - Press Enter: The webpage will open in a new editor tab within VS Code.
    
- Modify the `prompt.md` in the corresponding folder to test the chatbot. Note that an API key will be needed (will be provided on the study date). For example, 
    - Enter "Respond 'hello world' when I say hi" inside `outlineassistant/prompt.md`, save it using `Cmd+S` (Mac) or `Ctrl+S` (Windows)
    - Enter "hi" for the chatbot Outline Assistant in browser, notice how it should say "hello world" back
    - The Trip Advisor doesn't repond like that (since it's build from the source prompt in `tripadvisor/prompt.md`).

On the actual study date, you can test your chatbot prompt in a similar procedure.


---

## Troubleshooting

**Contact us**: If you run into any issues, contact us (Christina Ma & Keyu He) via your course communication channel or email. See FAQs [here](https://docs.google.com/document/d/1---Zywg3Kzaiq-BiOPXJfuX83NEfevb3BPS7leVGaco/edit?usp=sharing).

- **"Please add your OpenAI API key"**: Ensure `chatbot/.env` exists and contains a valid `OPENAI_API_KEY`.
- **Port already in use**: Another process may be using port 5000; stop it or change the port in `chatbot.py`.
