from random import randint, random
from time import perf_counter


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


# & Human Readable Numbers
def f_human_readable_number(number):
    """Convert a number into a human-readable format."""
    abs_number = abs(number)
    if abs_number >= 1_000_000_000:
        return f"{number / 1_000_000_000:.2f} billion"
    elif abs_number >= 1_000_000:
        return f"{number / 1_000_000:.2f} million"
    elif abs_number >= 1_000:
        return f"{number / 1_000:.2f} thousand"
    else:
        return f"{number:.2f}"


# & Simple Counting Algorithm
def f_simple_counting_algorithm(source_list, memory_limit):
    unique_items_list = []
    for item in source_list:
        # Debug display list growth
        if debugging_state:
            print(unique_items_list)

        # // # Check memory limit
        # // if len(unique_items_list) >= memory_limit:
        # //     if debugging_state:
        # //         print(f"{unique_items_list} at max memory exit.")
        # //     return "!!! MAX MEMORY !!!"

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
                for item in destination_list[
                    :
                ]:  # Iterate over a shallow copy of destination list
                    if random() > probability_factor:
                        destination_list.remove(
                            item
                        )  # Remove the first occurance of item

    return destination_list, probability_factor


# * Main Loop
debugging_state = False
source_list_size = 1000000
source_max_int = 100
memory_limit = 50
probability_factor = 1
probability_scaling_factor = 0.25

# Initialize Source List
source_list = f_generate_source_list(source_list_size, source_max_int)
print(f"\nSource list \n{source_list}")

# Debugging
actual_unique_values = f_debug_uniques(source_list, memory_limit)
print(f"\nUnique values debug \n{actual_unique_values}")

# Run Naive
naive_start_time = perf_counter()
naive_uniques = f_simple_counting_algorithm(source_list, memory_limit)
naive_end_time = perf_counter()
naive_time = naive_end_time - naive_start_time

# Run CVM
cvm_start_time = perf_counter()
cvm_unique_values, final_probability_factor = f_cvm_algorithm(
    source_list, memory_limit, probability_factor, probability_scaling_factor
)
cvm_end_time = perf_counter()
cvm_time = cvm_end_time - cvm_start_time

# Research Summary
## Resources saved
print("\nResearch Results")
memory_reduction_percentage = memory_limit / source_list_size * 100
readable_memory_reduction = f_human_readable_number(memory_reduction_percentage)
print(
    f'The CVM uses {memory_reduction_percentage}% of the memory that a traditional "COUNT IF" method uses.'
)
## Execution Times
time_reduction_percentage = naive_time / cvm_time * 100
readable_time_reduction = f_human_readable_number(time_reduction_percentage)
print(f"And is approximately {time_reduction_percentage:.1f}% faster.")
# Error Rate
estimate_uniques = len(cvm_unique_values) / final_probability_factor
current_error_rate_percent = round(
    ((abs(estimate_uniques - len(actual_unique_values))) / len(actual_unique_values))
    * 100,
    2,
)
print(f"Current error rate = {current_error_rate_percent}%")

print()
