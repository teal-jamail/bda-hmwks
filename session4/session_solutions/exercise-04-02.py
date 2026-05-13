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
    idx, url = item

    # Unique filenames prevent worker collisions when saving in parallel.
    input_path = os.path.join("images", f"image_{idx}.jpg")
    output_path = os.path.join("processed", f"rotated_image_{idx}.jpg")

    urllib.request.urlretrieve(url, input_path)

    image = Image.open(input_path)
    rotated = image.rotate(90, expand=True)
    rotated.save(output_path)


def serial_runner(urls):
    start = time.perf_counter()

    for idx, url in enumerate(urls, start=1):
        download_and_rotate((idx, url))

    end = time.perf_counter()
    print(f"Serial time: {end - start:.2f}s")


def pool_runner(urls, workers=4):
    start = time.perf_counter()

    # map expects one iterable of items, so we pack (idx, url) tuples first.
    items = list(enumerate(urls, start=1))
    with mp.Pool(processes=workers) as pool:
        pool.map(download_and_rotate, items)

    end = time.perf_counter()
    print(f"Pool time: {end - start:.2f}s")


if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    os.makedirs("processed", exist_ok=True)

    serial_runner(image_urls)
    pool_runner(image_urls, workers=4)
