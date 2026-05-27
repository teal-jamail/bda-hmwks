### Session 4 | Part 2

> In Part 2, you will use `multiprocessing.Pool` to process many image downloads in parallel.

#### 1. Goal

You will:

- understand how `multiprocessing.Pool` simplifies parallel execution
- run the same image-processing function over many inputs
- compare serial and pool-based execution time
- save processed images with unique filenames

#### 2. Prerequisites

From the `session4` folder:

1. Activate your virtual environment.

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

2. If `requirements.txt` is missing, create it with:

```txt
requests==2.32.3
Pillow
quizmd
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Windows PowerShell (after activation):

```powershell
pip install -r requirements.txt
```

#### 3. Mini tutorial (inline): `Pool.map(...)`

Create this warm-up file and add this code:

```txt
session4/solutions/exercise-04-02-warmup.py
```

```python
import multiprocessing as mp
import time


def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} finished")
    return f"Task {name} done"


if __name__ == "__main__":
    start = time.perf_counter()

    tasks = ["A", "B", "C", "D"]

    with mp.Pool(processes=4) as pool:
        results = pool.map(task, tasks)

    end = time.perf_counter()

    print(results)
    print(f"Total time: {end - start:.2f}s")
```

Run:

```bash
python3 solutions/exercise-04-02-warmup.py
```

What this shows:

1. `Pool` creates worker processes for you.
2. `pool.map(task, tasks)` applies `task` to each item.
3. Independent tasks can finish much faster in parallel than serial.

#### 4. Exercise

Create this file and complete it:

```txt
session4/solutions/exercise-04-02.py
```

Start from this baseline script (single image):

```python
from PIL import Image
import urllib.request

# Download a free sample image
url = "https://picsum.photos/300/200"
urllib.request.urlretrieve(url, "sample.jpg")

# Open the image
image = Image.open("sample.jpg")

# Rotate it 90 degrees
rotated_image = image.rotate(90, expand=True)

# Save the new image
rotated_image.save("rotated_sample.jpg")

print("Image rotated and saved as rotated_sample.jpg")
```

Use this URL list:

```python
image_urls = [
    "https://picsum.photos/id/10/300/200",
    "https://picsum.photos/id/20/300/200",
    "https://picsum.photos/id/30/300/200",
    "https://picsum.photos/id/40/300/200",
    "https://picsum.photos/id/50/300/200",
    "https://picsum.photos/id/60/300/200",
    "https://picsum.photos/id/70/300/200",
    "https://picsum.photos/id/80/300/200",
    "https://picsum.photos/id/90/300/200",
    "https://picsum.photos/id/100/300/200",
]
```

Network note:

- This exercise depends on internet access (`picsum.photos`).
- If a download fails, run the script again and compare timings only on successful runs.
- Treat temporary network errors separately from code correctness.

Complete this exercise in order:

1. Create `download_and_rotate(item)`:
   - `item` is a tuple: `(idx, url)`
   - download one image
   - rotate by 90 degrees
   - save with unique filename (for example `rotated_image_1.jpg`)
2. Create `serial_runner(urls)` that processes all URLs one by one.
3. In `pool_runner(urls, workers=4)`, build items with `enumerate(urls, start=1)` and use `mp.Pool(...).map(...)`.
4. Print serial time and pool time with `time.perf_counter()`.

Suggested skeleton:

```python
import multiprocessing as mp
import os
import time
import urllib.request

from PIL import Image


image_urls = [
    "https://picsum.photos/id/10/300/200",
    "https://picsum.photos/id/20/300/200",
    "https://picsum.photos/id/30/300/200",
    "https://picsum.photos/id/40/300/200",
    "https://picsum.photos/id/50/300/200",
    "https://picsum.photos/id/60/300/200",
    "https://picsum.photos/id/70/300/200",
    "https://picsum.photos/id/80/300/200",
    "https://picsum.photos/id/90/300/200",
    "https://picsum.photos/id/100/300/200",
]


def download_and_rotate(item):
    # item will be a tuple: (index, url)
    # TODO
    ...


def serial_runner(urls):
    start = time.perf_counter()
    # TODO
    ...
    end = time.perf_counter()
    print(f"Serial time: {end - start:.2f}s")


def pool_runner(urls, workers=4):
    start = time.perf_counter()
    # TODO
    ...
    end = time.perf_counter()
    print(f"Pool time: {end - start:.2f}s")


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    os.makedirs("processed", exist_ok=True)

    serial_runner(image_urls)
    pool_runner(image_urls, workers=4)
```

Run:

```bash
python3 solutions/exercise-04-02.py
```

Minimum completion checklist:

1. All 10 images are downloaded.
2. Rotated outputs are saved with unique names.
3. Both serial and pool timings are printed.
4. Script runs from `session4/` without path errors.

#### 5. Checkpoint questions

Answer briefly in comments at the bottom of your file:

1. Why is `Pool.map(...)` simpler than manual `Process` management?

   <details>
   <summary>Show answer</summary>

   `Pool.map(...)` handles worker creation and task distribution automatically, so you avoid manual `start()`/`join()` loops.

   </details>

2. Why should output filenames be unique in this exercise?

   <details>
   <summary>Show answer</summary>

   Without unique names, different workers can overwrite each other’s files and lose results.

   </details>

3. Why can this task benefit from parallelism?

   <details>
   <summary>Show answer</summary>

   Download + image processing includes waiting and independent work per image, so multiple workers can make progress at the same time.

   </details>

#### 6. Quiz

**Quiz 1**

```bash
quizmd quizzes/python-session-04-part-02-quiz.md
```

**Quiz 2 (Essay)**

```bash
quizmd quizzes/python-session-04-serial-vs-parallel-essay.md
```
