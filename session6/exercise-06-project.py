from concurrent.futures import ThreadPoolExecutor
from queue import Queue
import random
import threading
import time

printers = ["Printer-A", "Printer-B", "Printer-C"]

print_jobs = [
    "invoice_batch.pdf",
    "student_report.docx",
    "sales_chart.xlsx",
    "meeting_notes.pdf",
    "poster_draft.png",
    "research_summary.pdf",
    "attendance_sheet.csv",
    "budget_plan.xlsx",
    "slides_final.pptx",
    "lab_instructions.pdf",
]

message_lock = threading.Lock()

def log(message):
    with message_lock: 
        print(message)

# log() is wrapper for print(),
# locks print(), so only one thread at a time

def print_file(filename, available_printers):
    log(f"[WAITING] {filename} is waiting for printer")

    printer = available_printers.get() # blocks until available

    try:
        duration = random.uniform(1.0,3.0)
        log(f"[START] {filename} is printing on {printer}")
        time.sleep(duration)       # time: O(1) # space: O(1)
        log(f"[DONE] {filename} finished on {printer} in {duration: .2f}s")
    finally:
        available_printers.put(printer) # returns printer    

# fill queu with 3 printer names and start timer

if __name__ == "__main__":
    available_printers = Queue()

    for printer in printers:
        available_printers.put(printer)

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=len(print_jobs)) as executor:
        for filename in print_jobs:
            executor.submit(print_file, filename, available_printers)

    end = time.perf_counter()
    print(f"All print jobs finished in { end - start: .2f}s")

# .map for when every call takes exactly one argument from an iterable
# 'print_file' needs two args here [filename & available_printers]
        # .map can't easily pass the second - so w/ submit can pass any arg explicity