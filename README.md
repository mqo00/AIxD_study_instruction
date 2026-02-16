# AIxD Study Instruction

This repository supports the iterative tasks in AIxD study. To complete the study you need to (1) set up the environment, (2) use the task distribution interface, and (3) do your iterative tasks inside VSCode with GitHub Copilot Chat coding agent.


## 0. Setup before study date

Before starting, ensure you have the requirements (Python, VS Code, GitHub account, GitHub Copilot Pro access, Copilot Interaction Archiver, cloned repo) following the steps in **[SETUP.md](SETUP.md)**, and familiarize with the examples in **[DEMO.md](DEMO.md)**.

## 1. Instructions for the study

### 1. Sign up for a User ID

- Go to the sign-up [spreadsheet](https://docs.google.com/spreadsheets/d/1k1NB2U4cg0EI8wyyAaEuyDGk-BdKDXrjGumJo2b45C0/edit?usp=sharing); enter your Andrew ID next to a user ID to claim it.
- Prefer earlier IDs and ensure your chosen ID is not overwritten by others.

### 2. Get your task assignment

- Login to the task distribution system (link will be provided by the researcher on the study date). Do not start the pretest before finish reading all the instructions here. 
- When the system asks for your username, enter your signed-up user ID.

### 3. Task guidelines

- **One-off task**: Use the textbox on the Task Distribution System to enter your prompt directly.
- **Iterative task**: Follow Task Distribution System's instructions and use Copilot to develop iteratively in VS Code. See [DEMO.md: General Task Steps](DEMO.md#general-task-steps), [Game Task Demo](DEMO.md#game-task-demo) (**TicTacToe** and **Connect4**), and [Chatbot Task Demo](DEMO.md#chatbot-task-demo) (**Outline Assistant** and **TripAdvisor**).
    1. Open the corresponding task folder [as your workspace](https://code.visualstudio.com/docs/getstarted/getting-started#_open-a-folder-in-vs-code) in VS Code and select Yes to enable Copilot Interaction Archiver.
    2. Open [GitHub Copilot Chat](https://learn.microsoft.com/en-us/visualstudio/ide/visual-studio-github-copilot-chat?view=visualstudio#ask-questions-in-the-chat-window) and prompt Copilot to complete the task, your prompts will be automaticaly logged.
    3. For game task (detailed example in [Game Task Demo](DEMO.md#game-task-demo)), if games are implemented using python, you may run the game e.g., from the tictactoe folder's terminal, enter 
        ```bash
        python tictactoe.py
        ```
        For chatbot task (detailed example in [Chatbot Task Demo](DEMO.md#chatbot-task-demo)), launch the chatbot e.g., from the tripadvisor folder's terminal 
        ```bash
        python ../chatbot/chatbot.py
        ``` 
        Edit and save the corresponding `prompt.md` and test your prompt's effect using the chatbot via Simple Browser window at http://127.0.0.1:5000.


    4. When you finish the implementation, take a snapshot of your workspace

    


### 4. Start screen recording

- **Start recording your screen (desktop)** using Zoom before starting the study so we can see the websites and tools you used during the study. 
- Close unnecessary tabs and apps that you do not want to be recorded.
- Submit your zoom recording link in a google form when it's available (link will be provided by the researcher on the study date).
