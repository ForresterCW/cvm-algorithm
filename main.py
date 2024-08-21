# To build my version of the CVM algorithm, and visualize/explore the effects that the law of large numbers has on the error rates. 

from enum import unique
from itertools import count
from random import randint

# Generate a source list of random IDs
def f_random_list(list_size, max_int):
    random_list = []
    for i in range(1, list_size + 1):
        random_number = randint(1, max_int)
        random_list.append(random_number)
    if debugging_state:
        print(f"{random_list} = source list")
        print()
    return random_list

# Simple unique counting algorithm with memory checking and debug display
def f_simple_Counting_algorithm(source_list, memory_limit):
    unique_items_list = []
    for item in source_list:
        # Debug display list growth
        if debugging_state:
            print(unique_items_list)

        # Check memory limit        
        if len(unique_items_list) >= memory_limit:
            if debugging_state:
                print(f"{unique_items_list} at max memory exit.")
            return "!!! MAX MEMORY !!!"

        # Add item to unique_items_list if it isnt there
        if item not in unique_items_list:
            unique_items_list.append(item)
    return unique_items_list

# Advanced CVM algorithm with memory checking and debug display


# Main Loop
debugging_state = True
# debugging_state = False
source_list_size = 10
source_max_int = 10
memory_limit = 10
probability_factor = 1
probability_scaling_factor = 0.5

## Generate Source List
source_list = f_random_list(source_list_size, source_max_int)

## Baseline Counting Algorithm 
# baseline_unique_items_list = f_simple_Counting_algorithm(source_list, memory_limit)

## Advanced CVM algorithm



# Workshop
# Advanced CVM algorithm with memory checking and debug display

def f_OUTDATED_cvm_algorithm(source_list, memory_limit, probability_factor):
    if probability_factor == 1:
        # Simple counting algorithm 
        unique_items_list = []
        for item in source_list:
            # Debug display list growth
            if debugging_state:
                print(unique_items_list)

            # Check memory limit        
            if len(unique_items_list) >= memory_limit:
                if debugging_state:
                    print(f"{unique_items_list} at max memory exit.")
                print("!!! MAX MEMORY !!!")
                break

            # Add item to unique_items_list if it isnt there
            if item not in unique_items_list:
                unique_items_list.append(item)
    
    # Iterate probability factor
    probability_factor = probability_factor * probability_scaling_factor
    print(f"Memory Full, new probability factor is {probability_factor}")

    # Start the probabalistic CVM counting algo
    print("test")


# This should be consolodated.

def f_cvm_algorithm(source_list, memory_limit, probability_factor):
    unique_items_list = []

    # Integrate the probability factor from the beginning. If memory fails, iterate probabiloity factor and continue
    for item in source_list:
        # Debug display
        if debugging_state:
            print(unique_items_list)

        # Check memory limit        
        if len(unique_items_list) >= memory_limit:
            if debugging_state:
                print(f"{unique_items_list} at max memory exit.")
            print("!!! MAX MEMORY !!!")
                




f_cvm_algorithm(source_list, memory_limit, probability_factor)