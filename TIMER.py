import time

def countdown():
    n = int(input("Enter seconds to countdown: "))
    while n > 0:
        print(n)
        time.sleep(1)
        n -= 1
    print("Time's up! ⏰")

countdown()