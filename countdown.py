import time
import io
countDown = 100
while (countDown >= 0):
    print(countDown)
    countDown = countDown - 1
    time.sleep(0.0)
    if countDown == 0:
        print("KABOEM!!")
        print(inhoud)
        break