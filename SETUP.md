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


## 4. Configure the chatbot for iterative chatbot tasks

**Create your `.env` file**
   - Copy `chatbot/.env.example` to `chatbot/.env` (or rename).
   - Open `chatbot/.env` and set your LiteLLM API key (researcher will provide a key on the study date):

   ```
   LITELLM_API_KEY=your-litellm-api-key-here
   ```

---

## Troubleshooting

**Contact us**: If you run into any issues, contact Christina Ma via your course communication channel or email. See FAQs [here](https://docs.google.com/document/d/1---Zywg3Kzaiq-BiOPXJfuX83NEfevb3BPS7leVGaco/edit?usp=sharing).

- **"Please set LITELLM_API_KEY"**: Ensure `chatbot/.env` exists and contains a valid `LITELLM_API_KEY`.
- **Port already in use**: Another process may be using port 5000;
    - Ctrl+C in running process to quit,
    - kill it (check the pid by `lsof -i :5000` then `kill <pid>`), or
    - change the port in `chatbot.py`.
