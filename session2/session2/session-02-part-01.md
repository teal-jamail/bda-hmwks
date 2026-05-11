### Session 2 | Part 1

> In Part 1, you will prepare Gemini API access and complete a set of quizzes. You will reuse the Gemini key later while coding.

#### 1. Goal

You will:

- create a free API key in Google AI Studio
- complete a set of quizzes

#### 2. Prerequisites

Before starting:

1. In Visual Studio Code terminal, update your local repository (do this each time before you start, since new updates may be available).

Full repository update, recommended:

```bash
git pull origin main
```

**Do not run this.** Keep it as an option to refresh only session material when needed.

```bash
git fetch origin
git restore --source origin/main --staged --worktree session2
git clean -fdn session2
# Review the preview first, then run:
git clean -fd -e session2/solutions session2
```

> [!WARNING]
> `git clean` deletes untracked files. Keep your own work inside `session2/solutions` and use the command above with `-e session2/solutions` to protect it.

2. Open the `session2` folder in Visual Studio Code and in terminal.

```
cd session2
```

3. Create `python3 -m venv .venv` and activate your virtual environment:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Install requirements:

```bash
pip install -r requirements.txt
```

#### 3. Create API key (free)

Go to Google AI Studio, login using your personal gmail account and create an API key:

- https://aistudio.google.com/app/api-keys
- Add a name (or keep the default) and choose `Default Gemini Project`.
- Create a key and keep it private.
- Copy the API key (for example, `AIza...`).

#### 4. Set API key in terminal

Return to your Visual Studio Code terminal. On macOS/Linux, run the following command (replace with your API key):

```bash
export GEMINI_API_KEY="PASTE_YOUR_KEY"
```

On Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="PASTE_YOUR_KEY"
```

> [!TIP]
> You can either use an `OPENAI_API_KEY` if you have one. Gemini is free to use, but there are some limits.
 
**Test key is set**

Run this quick check in your terminal:

```bash
python3 -c 'import os; k=os.getenv("GEMINI_API_KEY"); print("GEMINI_API_KEY set:", bool(k)); print("Key length:", len(k) if k else 0)'
```

If `GEMINI_API_KEY set: True` appears and key length is greater than 0, your environment variable is working. Clear your terminal using `clear`, and let's proceed.

**Limits note**

Google AI Studio is free, but it has usage limits (typically 5-15 requests per minute, depending on the model).

> [!TIP]
>
> Limits depend on model and tier, and can change over time.
>
> Check the latest limits before running: https://ai.google.dev/gemini-api/docs/quota. If you exceed limits, you may receive `429` errors until quota resets.

#### 5. Complete the quizzes

**Essay quizzes**

Essay quizzes are a way for you to share your thoughts and have AI evaluate your answer against Stelios's approach to solving the problem. Read the instructions carefully before you start.

- Type your answer in the prompt.
- Press `Enter` for a new line.
- Type `/end` on its own line to finish.
- AI will then evaluate your answer.

**Make your terminal window larger for better visibility.**

Essay quiz 1:

```bash
quizmd quizzes/python-data-cleaning-tradeoff-essay.md
```

Essay quiz 2:

```bash
quizmd quizzes/python-complexity-basics-essay.md
```

**Debug quizzes**

A debug quiz helps you find and fix errors in code. Read each prompt carefully before you start editing. Change only what is needed, line by line. Use hints if you get stuck.

Rules:

- Press `D` or `d` to unlock the editor and fix the code
- Line numbers are shown by default
- Press `Esc` to open actions
- In actions, choose Proceed or Show hint with `↑/↓`, then press `Enter`
- The hint points to the line where the error exists
- Press `Ctrl+C` to exit at any time
- Follow code style. Use spaces around operators, for example: `x = 0` (not `x= 0`).

Try it out:

```bash
quizmd quizzes/python-session-01-debug-quiz.md
```
