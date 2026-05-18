# ── PART 2: multiprocess.Pool ───────────────────

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
    # item is tuple (idx, url); first unpack
    idx, url = item
    # Step 1: download & save image to 'images/' folder
    urllib.request.urlretrieve(url, f"images/image_{idx}.jpg")
    # Step 2: open downloaded img w/ Pillow
    image = Image.open(f"images/image_{idx}.jpg")
    # Step 3: rotate 90 degrees & save to 'processed/' folder
    rotated = image.rotate(90, expand = True)
    rotated.save(f"processed/rotated_img_{idx}.jpg")

def serial_runner(urls):
    start = time.perf_counter()

    # build items & pair ea. URL w/ index start at 1
    items = list(enumerate(urls, start=1))
    # gives [(1, url1), (2, url2), (3, url3)...]

    for item in items:
        download_and_rotate(item)

    end = time.perf_counter()
    print(f"Serial time: {end - start:.2f}s")

def pool_runner(urls, workers=4):
    start = time.perf_counter()

    #    1: tell how many worker procesess
    #    2: give func. & list of inputs
    #    'with' pool auto closes and cleans after done
    items = list(enumerate(urls, start=1))
    with mp.Pool(processes=workers) as pool:
            pool.map(download_and_rotate, items)

    end = time.perf_counter()
    print(f"Pool time: {end - start: .2f}s")

if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    os.makedirs("processed", exist_ok=True)
    serial_runner(image_urls)
    pool_runner(image_urls, workers=4)