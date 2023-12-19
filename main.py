import helpers.function_selector as selector
from time import process_time

# get user input
print("Which day would you like to run?\n")
print("[1]  [2]  [3]  [4]  [5]")
print("[6]  [7]  [8]  [9]  [10]")
print("[11] [12] [13] [14] [15]")
print("[16] [17] [18] [19] [20]")
print("[21] [22] [23] [24] [25]\n")
day = input("Enter Number: ")

print("Which part would you like to run?\n")
print("[1]")
print("[2]\n")
part = input("Enter Number: ")

# time start (only counts the time it takes to run the selected function)
start = process_time()

# set selected function
res = selector.dict[day]["function"](part)

# time stop
stop = process_time()
ms = round((stop - start) * 1000, 2)

# print input
print(f"Time to process is {ms}ms")
print(f"Result: {res}")
