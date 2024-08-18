# To build my version of the CVM algorithm, and visualize/explore the effects that the law of large numbers has on the error rates. 

from random import randint

# Generate a source list of random IDs
def f_random_list(list_size, max_int):
    randomList = []
    for i in range(1, list_size + 1):
        random_number = randint(1, max_int)
        randomList.append(random_number)
    return randomList

# Check if memory is full (pass/fail)
def f_memory_check(active_list, memory_limit):
    if len(active_list) < memory_limit:
        return "pass"
    if len(active_list) >= memory_limit:
        return "fail"

# Simple counting algorithm 


# Main Loop
memory_limit = 10

## Generate source list
source_list = f_random_list(10, 10)
print(source_list)
