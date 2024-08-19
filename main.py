# To build my version of the CVM algorithm, and visualize/explore the effects that the law of large numbers has on the error rates. 

from random import randint

# Generate a source list of random IDs
def f_random_list(list_size, max_int):
    randomList = []
    for i in range(1, list_size + 1):
        random_number = randint(1, max_int)
        randomList.append(random_number)
    return randomList

# Simple counting algorithm with memory checking built in
def f_simple_Counting_algorithm(source_list, memory_limit):
    unique_list = []
    for item in source_list:
        # Check memory limit
        if len(unique_list) >= memory_limit:
            if debugging_state:
                print(f"Final list at memory limit = {unique_list}")
            return "! Fatal Error: Memory Limit reached !"
        # Append source value to the unique list if it is not already there 
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Main Loop
debugging_state = True
# debugging_state = False

source_list_size = 10
source_max_int = 10
memory_limit = 10
probability_factor = 1

## Generate Source List
source_list = f_random_list(source_list_size, source_max_int)
if debugging_state:
    print(f"Debug source list =  {source_list}")

## Baseline Counting Algorithm 
baseline_uniques = len(f_simple_Counting_algorithm(source_list, memory_limit))
if debugging_state:
    print(f"Debug baseilne uniques = {baseline_uniques}")

## Advanced CVM algorithm







# Workshop
