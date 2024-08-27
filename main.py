from random import randint, random


# & Generate List of Random Numbers
def f_generate_source_list(list_size, max_int):
    random_list = []
    for i in range(1, list_size + 1):
        random_number = randint(1, max_int)
        random_list.append(random_number)
    return random_list


# & Debug Uniques
def f_debug_uniques(source_list, memory_limit):
    unique_items_list = []
    for item in source_list:
        # Add item to unique_items_list if it isnt there
        if item not in unique_items_list:
            unique_items_list.append(item)
    return unique_items_list


# & Simple Counting Algorithm
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


# & CVM Algorithm
def f_cvm_algorithm(
    source_list, memory_limit, probability_factor, probability_scaling_factor
):
    # Variables
    destination_list = []

    # Core Loop
    for item in source_list[
        :
    ]:  # Iterate over a copy of source_list to avoid modifying the list during iteration

        # Memory Check
        if len(destination_list) >= memory_limit:
            # Adjust probability factor
            probability_factor *= probability_scaling_factor

            # Iterate through destination list and randomly delete items based on the probability factor
            probability_index = 0
            while probability_index < len(destination_list):
                if random() < probability_factor:
                    del destination_list[probability_index]
                    # Do not increment index if an item was deleted
                else:
                    probability_index += 1

            continue  # Continue to the next item in source_list

        # If item is in destination_list, remove it from source_list
        if item in destination_list:
            continue  # Skip to the next item in source_list
        else:
            # Decide to add the item to destination_list based on a random chance
            if random() < probability_factor:
                destination_list.append(item)
            # If not added, just continue to the next item

    return destination_list, probability_factor


# * Main Loop
debugging_state = False
source_list_size = 100
source_max_int = 100
memory_limit = 5
probability_factor = 1
probability_scaling_factor = 0.5

# Initialize Source List
source_list = f_generate_source_list(source_list_size, source_max_int)
print(f"\nSource list \n{source_list}\n")

# Baseline
debug_unique_values = f_debug_uniques(source_list, memory_limit)
print(f"Baseline Unique Values \n{debug_unique_values}\n")

# Run CVM Algorithm
cvm_unique_values, final_probability_factor = f_cvm_algorithm(
    source_list, memory_limit, probability_factor, probability_scaling_factor
)
print(f" CMV Unique Values \n{cvm_unique_values}\n")
print(f"Probability factor \n{final_probability_factor}\n")
