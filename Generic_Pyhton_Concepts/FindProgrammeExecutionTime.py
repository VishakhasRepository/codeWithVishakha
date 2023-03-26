import time

initial = time.time()  # this gives time in tics/seconds
for item in range(45):
    print("Hello")
print(time.time() - initial)

k = 0
initial2 = time.time()
while (k < 45):
    print("Hello2")
    k = k + 1
print(time.time() - initial2)



#print local time

local_time = time.asctime(time.localtime(time.time()))   #time.localtime(time.time()) returns tuple and asctime converts into a format
print(local_time)  # Sun Apr 25 19:37:39 2021
