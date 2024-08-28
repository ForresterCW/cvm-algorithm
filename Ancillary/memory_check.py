# Single Function: Perform the CVM algorighm on a random source list.

from random import randint, random

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
                print(f"List going in = {destination_list}")
                # Scale probability
                probability_factor *= probability_scaling_factor

                # Down size destination list 
                for item in destination_list[:]:  # Iterate over a shallow copy of destination list
                    if random() > probability_factor:
                        destination_list.remove(item) # Remove the first occurance of item
                print(f"List coming out = {destination_list}")
        
    # Estimate the # of uniques 
    print(f"Estimate of uniques = {len(destination_list) * (1 + probability_factor)}")

    return destination_list




# When you remove an item from the list, the remaining items shift their positions. The loop, however, continues to the next index, potentially skipping elements or causing an incorrect iteration.
        # ! Memory check and down sizing 
        # if len(destination_list) > memory_limit:
        #     print(f"List going in = {destination_list}")
        #     # Scale probability
        #     probability_factor *= probability_scaling_factor

        #     # Down size destination list 
        #     for item in destination_list:
        #         if random() > probability_factor:
        #             destination_list.remove(item)
        #     print(f"List coming out = {destination_list}")





print(f"Source list = {source_list} = {10}")

print(
    f_cvm_algorithm(
        source_list, memory_limit, probability_factor, probability_scaling_factor
    )
)

# Estimate the # of uniques 
