import time
import io
countDown = 20
while (countDown >= 0):
    print(countDown)
    countDown = countDown - 1
    time.sleep(0.5)
    if countDown == 0:
        print("done")
        break