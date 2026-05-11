### Session 2 | Homework

> In this homework, you will treat Gemini as a black-box function: input prompt -> output text. Then you will use that function to help clean missing values in a dataset.

#### 1. Goal

You will:

- create a free API key in Google AI Studio (if you don't already have one)
- call Gemini from Python using one reusable function
- load `studio_ghibli_movies.csv`
- use AI to fill missing fields
- save a cleaned dataset to disk

#### 2. Prerequisites

From `session2/`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

#### 3. Create API key (free)

Go to Google AI Studio:

- https://aistudio.google.com/app/api-keys
- Add a name and choose `Default Gemini Project`
- Copy your API key

Set it in terminal:

```bash
export GEMINI_API_KEY="PASTE_YOUR_KEY"
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="PASTE_YOUR_KEY"
```

Quick check:

```bash
python3 -c 'import os; k=os.getenv("GEMINI_API_KEY"); print("GEMINI_API_KEY set:", bool(k)); print("Key length:", len(k) if k else 0)'
```

#### 4. Limits note

Google AI Studio is free, but it has usage limits.

> Limits depend on model and tier and can change over time. Check latest limits: https://ai.google.dev/gemini-api/docs/quota. If you exceed limits, you may see `429` errors until quota resets.

#### 5. Download dataset

Use: [Birkbeck/studio_ghibli_movies](https://huggingface.co/datasets/Birkbeck/studio_ghibli_movies)

```bash
hf download Birkbeck/studio_ghibli_movies studio_ghibli_movies.csv \
  --repo-type dataset \
  --local-dir .
```

#### 6. Gemini function

Create:

```txt
session2/solutions/exercise-02-homework.py
```

Use this function as your AI helper.

- This function uses a Gemini model and calls it remotely over the internet (API call).
- For this homework, do not worry about all implementation details yet.
- Treat this as a black box for now: prompt in, answer out.

```python
import json
import os
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def ask_gemini(prompt, model_name="gemini-2.5-flash"):
    # Read your API key from the environment.
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    # Build the remote Gemini endpoint URL.
    url = (
        "https://generativelanguage.googleapis.com/v1beta/models/"
        f"{model_name}:generateContent"
    )

    # Prepare the request body with your prompt.
    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    # Create an HTTP POST request with JSON payload and API key.
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
        method="POST",
    )

    # Send request, parse JSON response, and return only model text.
    # If quota/rate limit is reached, show a student-friendly message.
    try:
        with urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except HTTPError as err:
        if err.code == 429:
            raise RuntimeError(
                "Gemini rate/limit reached. Please wait a minute and try again."
            ) from err
        raise

    return data["candidates"][0]["content"]["parts"][0]["text"].strip()
```

Tip:
- Be careful with Gemini limits.
- `gemini-2.5-flash` is a current model today, but this may change in the future.
- Check the latest docs online before running: https://ai.google.dev/gemini-api/docs/models
- Check quota/limits here: https://ai.google.dev/gemini-api/docs/quota
- If you get a limit error (`429`), wait a minute and try again.

Now call it like this:

```python
answer = ask_gemini("Your prompt here")
print(answer)
```

#### 7. Prompt examples (strict output)

Ask for strict format so parsing is easier.

Example: year only

```txt
Return only the 4-digit release year for the Studio Ghibli movie "Ponyo".
Output format: only 4 digits, no extra text.
```

Example: composer only

```txt
Return only the composer full name for the Studio Ghibli movie "Howl's Moving Castle".
Output format: name only, no extra text.
```

#### 8. Homework task

In `session2/solutions/exercise-02-homework.py`:

1. Load `studio_ghibli_movies.csv` using `csv.DictReader`.
2. Find rows with missing `year`.
3. For each missing `year`, call `ask_gemini(...)` and fill value.
4. Find rows with missing `music_by`.
5. For each missing `music_by`, call `ask_gemini(...)` and fill value.
6. Save output file as `studio_ghibli_movies_ai_clean.csv`.
7. Print:
   - how many values were filled by AI
   - any rows still missing values

Keep it simple. You are using Gemini as a helper function, not building a full framework.

#### 9. Submission

Include:

- `session2/solutions/exercise-02-homework.py`
- optional: `studio_ghibli_movies_ai_clean.csv`
