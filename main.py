import days.day01 as calibrator
from time import process_time

# time start
start = process_time()

# functions here (comment out all functions you are not testing for accurate process time)
day01 = calibrator.calibrate()

# time stop
stop = process_time()

# print input
ms = round((stop - start) * 1000, 2)
print(f"Time to process is {ms}ms")
print(f"Result: {day01}")
