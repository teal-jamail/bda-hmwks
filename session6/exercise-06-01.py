from concurrent.futures import ThreadPoolExecutor
import threading

from faker import Faker
# Rule: one lock, defined once at top
# only for shared resource (critical section)

fake = faker = Faker()
write_lock = threading.Lock()

def generate_phrase():
    return fake.sentence(nb_words=6)
    # Time O(1) # Space: O(1)

def save_phrase(index):
    phrase = generate_phrase()

    with write_lock: # Time O(1) # Space: O(1)
        with open("generated_phrases.txt", "a", encoding="utf-8") as file:
            file.write(f"Phrase {index}: {phrase}\n")

    print(f"Saved phrase {index}: {phrase}")

# open file with "a" (append) mode
# "w" would truncate file to empty ea. time thread opened it

# --- Main Block---
# clear file before starting
# spin up 10 workers
# map 'save_phrase' across indices 1 to 11

# Clear by opening file in "w" and then closing

if __name__ == "__main__":
    with open ("generated_phrases.txt", "w", encoding="utf-8"):
        pass

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(save_phrase, range (1, 11))
        # Time: O(n) # Space O(n)

    print("Done. Check generated_phrases.txt")

