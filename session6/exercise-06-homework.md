# Session 6 Homework

## Capstone repository

Link: https://github.com/teal-jamail/bda-capstone-1

## New YouTube URLs

1. https://www.youtube.com/watch?v=dQw4w9WgXcQ
2. https://www.youtube.com/watch?v=aqz-KE-bpKQ
3. https://www.youtube.com/watch?v=YE7VzlLtp-4
4. https://www.youtube.com/watch?v=TLkA0RELQ1g
5. https://www.youtube.com/watch?v=R6MlUcmOul8

## What I changed

* Added 5 new YouTube URLs to data/video_urls.csv. 
* Replaced the multiprocessing section with a ThreadPoolExecutor running 10 workers. 
* Added a new function download_with_semaphore() that wraps each download in a semaphore block limiting active downloads to 5 at a time.

## Semaphore design

Two separate synchronisation objects were used. download_limit = threading.Semaphore(5) wraps the actual download call — only 5 threads can be inside that block at once. result_file_guard = threading.Semaphore(1) wraps the file write — only one thread writes a result line at a time. They are separate because limiting downloads and protecting file writes are two different coordination problems.

## Result file format

## Testing

Confirmed the semaphore held at 5 by reading the terminal output — exactly 
5 START messages appeared before any DONE message. Once one download finished 
and released its permit, the 6th START appeared immediately.

## Reflection

Safely writing results was harder. Limiting downloads required one semaphore around the download call. But writing results needed a separate lock, and I had to understand that holding the download semaphore during file writing would unnecessarily block other threads. Keeping the two concerns separate was the key insight.