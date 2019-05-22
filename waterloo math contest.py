import math
import time

start_time = time.time()

for x in range(1, 51):
    for y in range(1, 51):
        if (x + y) / 2 - math.sqrt(x * y) == 1 and x < y:
            print(x, y)

print("---program finished in %s second ---" % (time.time() - start_time))
