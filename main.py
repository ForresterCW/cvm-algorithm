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

    return destination_list, probability_factor


# * Main Loop
debugging_state = False
source_list_size = 1000000
source_max_int = 1000
memory_limit = 50
probability_factor = 1
probability_scaling_factor = 0.25

# Initialize Source List
source_list = f_generate_source_list(source_list_size, source_max_int)
print(f"\nSource list \n{source_list}")

# Baseline
actual_unique_values = f_debug_uniques(source_list, memory_limit)
print(f"\nBaseline Unique Values \n{actual_unique_values}")

# Run CVM Algorithm
cvm_unique_values, final_probability_factor = f_cvm_algorithm(
    source_list, memory_limit, probability_factor, probability_scaling_factor
)
print(f"\nCVM Unique Values \n{cvm_unique_values}")
print(f"\nProbability factor \n{final_probability_factor}\n")

# Estimate unique values 
estimate_uniques = len(cvm_unique_values) / final_probability_factor
print(f"\nEstimated unique values = {estimate_uniques}")
print(f"Actual unique values = {len(actual_unique_values)}")

# Current error rate 
#// current_error_rate_percent = round((estimate_uniques / len(actual_unique_values)) * 100)
#// print(f"\nCurrent error rate = {current_error_rate_percent}% correct")
    # Calculate the absolute difference between estimated and actual unique values
absolute_difference = abs(estimate_uniques - len(actual_unique_values))
    # Express the absolute difference as a percentage of the actual unique values
current_error_rate_percent = round((absolute_difference / len(actual_unique_values)) * 100, 2)
print(f"\nCurrent error rate = {current_error_rate_percent}%")


print()
