from datetime import datetime
import time

now = datetime.now()

print(f"Day: {now.strftime('%A')}")
print(f"Time: {now.strftime('%H:%M:%S')}")
print(f"Timestamp: {time.time():.2f}")