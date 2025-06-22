import subprocess
import time

for i in range(5):
    print(f"Running complete.py (iteration {i + 1})...")
    subprocess.run(["python", "complete.py"])
    time.sleep(2)

print("All runs completed.")
