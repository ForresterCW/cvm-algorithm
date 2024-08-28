# Single Function: Perform the CVM algorighm on a random source list.

from random import randint, random

# & Simple CVM Algo
# Variables
# source_list = debug_source_list = [1,2,3,4,5,6,7,8,9,10]
source_list = debug_source_list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
memory_limit = 5
probability_factor = 1
probability_scaling_factor = 0.5


def f_cvm_algorithm(
    source_list, memory_limit, probability_factor, probability_scaling_factor
):
    # Variables
    destination_list = []

    # Perform CVM on every item in source list
    for item in source_list:

        # Remove value if it is in destination list
        if item in destination_list:
            destination_list.remove(item)
        
            # Coin flip to store in destination list
            if random() <= probability_factor:
                destination_list.append(item)

        # Coin flip to store in destination list
        else:
            if random() <= probability_factor:
                destination_list.append(item)

        # ! Memory check and down sizing 
            if len(destination_list) > memory_limit:

                # Scale probability
                probability_factor *= probability_scaling_factor

                # Down size destination list 
                for item in destination_list[:]:  # Iterate over a shallow copy of destination list
                    if random() > probability_factor:
                        destination_list.remove(item) # Remove the first occurance of item
        
    return destination_list


print(
    f_cvm_algorithm(
        source_list, memory_limit, probability_factor, probability_scaling_factor
    )
)
