# Two coordination problems:
# 1. limiting concureent requests
# 2. protect shared results file
# -- Requires seperate locks
#       - Semaphore manages concurrency
#       - Lock manages exclusivity

from concurrent.futures import ThreadPoolExecutor
import threading
import time

import requests

call_limit = threading.Semaphore(4)
# max 4 active requressts
write_lock = threading.Lock()
# 1 thread writes 1 file at a time

def fetch(request_id):
    url = f"https://httpbin.org/delay/1?request={request_id}"
    
    with call_limit:        # Time & Space - O(1)
        print(f"[START] requests {request_id:02d}")

        try:
            response = requests.get(url, timeout = 10)
            status = f"success status = {response.status_code}"
        except requests.RequestException as exc:
            status = f"failed error = {exc}"

        print(f"[DONE] request {request_id:02d}")

    with write_lock:
        with open("request_results.txt", "a", encoding="utf-8") as file:
            file.write(f"request={request_id:02d} {status}\n")

# 02d - format int w/ min. 2 digit, pading w/ zero on left if needed
#       -- request 1 becomes 01 ...to 10 [for readability]


# --- Main Block---  
if __name__ == "__main__":
    with open("request_results.txt", "w", encoding="utf-8"): # clear file
        pass

    start = time.perf_counter()

    with ThreadPoolExecutor (max_workers = 40) as executor: # Time & Space: O(n)
        executor.map(fetch, range(1, 41))

    end = time.perf_counter()
    print(f"Total time: {end - start: .2f}s")
    print("Done. Check request_results.txt")

# max_workers=40 means all 40 tasks get submitted and ready to run
# the semaphore controls concurrently active workers 