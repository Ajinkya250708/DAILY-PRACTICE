import time

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    elapsed = end - start
    print(f"Time elapsed: {elapsed:.2f} seconds")

stopwatch()