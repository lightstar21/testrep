import time

# Configuration
WORD = "gold, "
NUM_REPEATS = 14_000_000
FILENAME = "gold.txt"
SLEEP_DURATION = 4  # Seconds to sleep between overwrites to avoid hogging resources (adjust as needed)

# First, write the word repeatedly to the file 14 million times (efficiently)
print(f"Writing '{WORD}' {NUM_REPEATS:,} times to {FILENAME}...")
content = (	WORD) * NUM_REPEATS
with open(FILENAME, 'w') as f:
    f.write(content)
print("Initial write completed.")


# Then, repeatedly overwrite the same file with the same content in a loop,
# but with a sleep delay to prevent excessive CPU/disk usage
print(f"Starting overwrite loop with {SLEEP_DURATION}-second delays...")
iteration = 1
while True:
    #print(f"Overwrite iteration {iteration} starting...")
    start_time = time.time()
    with open(FILENAME, 'w') as f:
        f.write(content)
    end_time = time.time()
    duration = end_time - start_time
    #print(f"Overwrite iteration {iteration} completed in {duration:.2f} seconds.")
    #print(f"Sleeping for {SLEEP_DURATION} seconds...")
    time.sleep(SLEEP_DURATION)
    iteration += 1

# Note: This will run indefinitely until manually stopped (e.g., Ctrl+C).
# The sleep prevents rapid disk I/O and CPU spikes.
# Each overwrite still creates the ~100MB file, but now at a controlled rate.
# If you want even less resource use, increase SLEEP_DURATION or reduce NUM_REPEATS.
# For naive individual writes (very slow/resource-intensive), avoid the bulk write.

