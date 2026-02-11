# AIxD Study Instruction

This repository supports the iterative tasks in AIxD study. To complete the study you need to (1) set up the environment, (2) use the task distribution interface, and (3) do your iterative tasks inside VSCode with GitHub Copilot Chat coding agent.


## 0. Setup before study date

Before starting, ensure you have the requirements (Python, VS Code, GitHub account, GitHub Copilot Pro access, Copilot Interaction Archiver, cloned repo) following the steps in **[SETUP.md](SETUP.md)**.

## 1. Instructions for the study

### 1. Sign up for a User ID

- Go to the sign-up [spreadsheet](https://docs.google.com/spreadsheets/d/1k1NB2U4cg0EI8wyyAaEuyDGk-BdKDXrjGumJo2b45C0/edit?usp=sharing); enter your Andrew ID next to a user ID to claim it.
- Prefer earlier IDs and ensure your chosen ID is not overwritten by others.

### 2. Get your task assignment

- Login to the task distribution system (link will be provided by the researcher on the study date). Do not start the pretest before finish reading all the instructions here. 
- When the system asks for your username, enter your signed-up user ID.

### 3. Task guidelines

- **One-off task**: Use the textbox on the Task Distribution System to enter your prompt directly.
- **Iterative task**: Follow Task Distribution System's instructions and use Copilot to develop iteratively in VS Code. See [SETUP.md: Test run the extensions and Copilot](SETUP.md#test-run-the-extensions-and-copilot).
    1. Open the corresponding task folder as your workspace in VS Code.
        - e.g., if you are assigned with TicTacToe (Iterative), select the `AIxD_study_instruction/tictactoe` folder to [open as your workspace](https://code.visualstudio.com/docs/getstarted/getting-started#_open-a-folder-in-vs-code) in VS Code
        - Click `Yes` to Enable Copilot Interaction Archiver for this workspace.
    2. Open [GitHub Copilot Chat](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=visualstudio#ask-questions-in-the-chat-window) coding agent by selecting `View` > `GitHub Copilot Chat` or clicking the Copilot icon inside VS Code.
        - Prompt Copilot to complete the task, your prompts will be automaticaly logged.
    3. When you finish the implementation, **take a snapshot of your workspace** by clicking the "Archiver: {yourid}" button at the bottom right corner of VS Code and then click `Capture Repo Snapshot` 

- **Iterative Chatbot tasks**: The repo includes starter code for a chatbot used for the **Outline Assistant** and **TripAdvisor** tasks. See [SETUP.md: Test run the chatbot](SETUP.md#test-run-the-chatbot).
    - Inside `AIxD_study_instruction/chatbot/.env`, paste in the researcher-provided OPENAI API key. 
    - Open the corresponding task folder as your workspace in VS Code, e.g., `AIxD_study_instruction/outlineassistant`, depending on your task assignment.
    - Open a terminal in your VSCode workspace and launch the chatbot
        ```bash
        python ../chatbot/chatbot.py
        ```
    - Open a browser window at http://127.0.0.1:5000. Or press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows) to open the Command Palette; type and run: `Simple Browser: Show` to paste the url. 
    - Choose the chatbot according to your task assignment. E.g., the Outline Assistant chatbot uses the system prompt from `outlineassistant/prompt.md`.
    - Open [GitHub Copilot Chat](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=visualstudio#ask-questions-in-the-chat-window) coding agent by selecting `View` > `GitHub Copilot Chat` or clicking the Copilot icon inside VS Code.
    - Interact with Copilot to build your chatbot prompt in the corresponding `prompt.md`. Save the file and view your prompt's effect using the chatbot.
    


### 4. Start screen recording

- **Start recording your screen (desktop)** using Zoom before starting the study so we can see the websites and tools you used during the study. 
- Close unnecessary tabs and apps that you do not want to be recorded.
- Submit your zoom recording link in a google form when it's available (link will be provided by the researcher on the study date).
