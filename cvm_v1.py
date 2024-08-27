from random import randint, random

debugging_state = True
debug_source_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
source_list = debug_source_list
source_list_size = 10
source_max_int = 10
memory_limit = 10
probability_factor = 1
probability_scaling_factor = 0.5


# ~ Workshop
# & My CVM algorithm attempt, kind of working
def f_cvm_algorithm(
    source_list, memory_limit, probability_factor, probability_scaling_factor
):
    # Variables
    destination_list = []

    # Core Loop
    for item in source_list:

        # Memory Check
        if len(destination_list) >= memory_limit:
            # Iterate probability factor
            probability_factor *= probability_scaling_factor
            print(f"!!Memory Limit!! New probability factor = {probability_factor}")
            # Probability coin flip
            probability_index = 0
            while probability_index < len(destination_list):
                if random() >= probability_factor:
                    del destination_list[probability_index]
                    # Do not increment probability_index, as list size has changed
                else:
                    probability_index += 1  # Only increment if no deletion
        else:
            # Add unique items to the destination list
            if item not in destination_list:
                destination_list.append(item)

        #
        if item in destination_list:
            del item
        else:
            if random() >= probability_factor:
                destination_list.append(item)
            else:
                break

    return destination_list


print(
    f_cvm_algorithm(
        source_list, memory_limit, probability_factor, probability_scaling_factor
    )
)
