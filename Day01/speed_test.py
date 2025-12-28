#loop time calculation

import time
n = 1000000
start = time.time()
count = 0
for i in range (n):
    count+= i
print(f" loop time {time.time() - start : 5f} seconds ")
