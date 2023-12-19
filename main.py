import helpers.function_selector as selector
from time import process_time
from colorama import Fore

# get user input
print("\nWhich day would you like to run?\n")
print(Fore.BLUE + "[1]  [2]  [3]  [4]  [5]")
print(Fore.BLUE + "[6]  [7]  [8]  [9]  [10]")
print(Fore.BLUE + "[11] [12] [13] [14] [15]")
print(Fore.BLUE + "[16] [17] [18] [19] [20]")
print(Fore.BLUE + "[21] [22] [23] [24] [25]\n")
day = input(Fore.YELLOW + "Enter Day: ")
print(Fore.WHITE + "----------------------------------------\n")

print(Fore.RED + f"[Day {day}]: " + Fore.WHITE + "Which part would you like to run?\n")
print(Fore.BLUE + "[1]")
print(Fore.BLUE + "[2]\n")
part = input(Fore.YELLOW + "Enter Part: ")
print(Fore.WHITE + "----------------------------------------\n")

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
