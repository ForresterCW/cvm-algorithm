# pip install -r requirements.txt

from random import randint, random
from time import perf_counter
import matplotlib.pyplot as plt
import statistics


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
# Variables
max_source_list_size = 1000
number_of_averages = 5
source_max_int = 100
master_memory_limit = 50
probability_factor = 1
probability_scaling_factor = 0.25
debugging_state = False

x_list_size = []
y_memory_reduction_percentages = []
y_time_reduction_percentages = []
y_error_rates = []

# ~ Research
current_iteration = 0
naive_time_averages = []
cvm_time_averages = []
error_rate_averages = []

for i in range(max_source_list_size):
    memory_limit = master_memory_limit
    current_iteration += 1
    x_list_size.append(current_iteration)
    if memory_limit > current_iteration:
        memory_limit = current_iteration
    else:
        memory_limit = master_memory_limit

    # Initialize source list
    iteration_source_list = f_generate_source_list(current_iteration, source_max_int)

    # Actual unique values
    actual_unique_values = f_debug_uniques(iteration_source_list, memory_limit)

    # 5x average of naive runtime
    for i in range(number_of_averages):
        naive_start_time = perf_counter()
        naive_uniques = f_simple_counting_algorithm(iteration_source_list, memory_limit)
        naive_end_time = perf_counter()
        naive_time = naive_end_time - naive_start_time
        naive_time_averages.append(naive_time)
    naive_average_time = statistics.median(naive_time_averages)
    # // # Non-averaged naive count if
    # // naive_start_time = perf_counter()
    # // naive_uniques = f_simple_counting_algorithm(iteration_source_list, memory_limit)
    # // naive_end_time = perf_counter()
    # // naive_time = naive_end_time - naive_start_time

    # 5x average of CVM runtime
    for i in range(number_of_averages):
        cvm_start_time = perf_counter()
        cvm_unique_values, final_probability_factor = f_cvm_algorithm(
            iteration_source_list,
            memory_limit,
            probability_factor,
            probability_scaling_factor,
        )
        cvm_end_time = perf_counter()
        cvm_time = cvm_end_time - cvm_start_time
        cvm_time_averages.append(cvm_time)
    cvm_average_time = statistics.median(cvm_time_averages)
    # // # Run CVM
    # // cvm_start_time = perf_counter()
    # // cvm_unique_values, final_probability_factor = f_cvm_algorithm(
    # //     iteration_source_list,
    # //     memory_limit,
    # //     probability_factor,
    # //     probability_scaling_factor,
    # // )
    # // cvm_end_time = perf_counter()
    # // cvm_time = cvm_end_time - cvm_start_time

    # Memory reduction results
    memory_reduction_percentage = round(memory_limit / current_iteration * 100)
    y_memory_reduction_percentages.append(memory_reduction_percentage)

    # Time reduction results
    time_reduction_percentage = round(naive_average_time / cvm_average_time * 100)
    # // Non-averaged
    # // time_reduction_percentage = round(naive_time / cvm_time * 100)
    y_time_reduction_percentages.append(time_reduction_percentage)

    # 5x average error rate
    for i in range(number_of_averages):
        estimated_unique_values = len(cvm_unique_values) / final_probability_factor
        current_error_rate_percent = round(
            (
                (abs(estimated_unique_values - len(actual_unique_values)))
                / len(actual_unique_values)
            )
            * 100,
            2,
        )
        error_rate_averages.append(current_error_rate_percent)
    averaged_error_rates = statistics.median(error_rate_averages)
    y_error_rates.append(averaged_error_rates)

# Plot research results
# // Non-Averaged
# // plt.plot(x_list_size, y_memory_reduction_percentages, label="x% Less Memory Used")
# // plt.plot(x_list_size, y_time_reduction_percentages, label="x% Faster Execution")
# Plot the original dual plot
(line1,) = plt.plot(
    x_list_size, y_memory_reduction_percentages, label="Memory Required (%)"
)
(line2,) = plt.plot(
    x_list_size, y_time_reduction_percentages, label="Faster Execution (%)"
)

# Create a new axis on the right for y_error_rates
ax1 = plt.gca()  # Get the current axis
ax2 = ax1.twinx()  # Create a twin axis sharing the same x-axis

# Plot y_error_rates on the new axis with new step values
(line3,) = ax2.plot(
    x_list_size, y_error_rates, color="green", linestyle="--", label="Error Rate (%)"
)

# Set labels for the axes
ax1.set_xlabel("X Axis Label")
ax1.set_ylabel("Memory / Time Reduction (%)")
ax2.set_ylabel("Error Rate (%)")

# Combine the legends into one
lines = [line1, line2, line3]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper center")

# Show the plot
plt.show()
