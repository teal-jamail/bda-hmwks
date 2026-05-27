## Welcome to Session 4

### Learning goals

By the end of Session 4, you should be able to:

- explain serial execution vs process-based parallel execution
- use `multiprocessing.Process` with `start()` and `join()`
- use `multiprocessing.Pool` for cleaner parallel workflows
- compare serial vs parallel performance on practical tasks

### Recommended order

1. [Part 1](./session-04-part-01.md)
2. [Part 2](./session-04-part-02.md)
3. Write your own work in [solutions](./solutions/).
4. Review [reference solutions](./session_solutions/) only after attempting tasks yourself.
5. Practice with [quizzes](./quizzes/) when ready.

### Notes

- Tutorial and warm-up material is included directly inside each part markdown file.
- Keep your own solutions in separate files inside `solutions/`.
- Use exercise-style names in `solutions/` (for example `exercise-04-01.py`, `exercise-04-02.py`).
- Create your files inside `solutions/` as you work through each part.
- Reference answers are in `session_solutions/`.
- Use `if __name__ == "__main__":` in multiprocessing scripts.
- If `requirements.txt` is missing, create it and add:
  - `requests==2.32.3`
  - `Pillow`
  - `quizmd`
- Keep all dependencies in `requirements.txt`, then install with:
  - `pip install -r requirements.txt`
