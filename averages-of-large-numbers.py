# Goal: To see how the average changes as the number of random numbers increases.
# Prediction: As random numbers -> inf, avg / (source list / 2) = 1

import random

# Simulate a unique data stream into a source list
def f_generate_source_list(target_list, size):
    """
    Generate a list of random integers and append them to the target list.

    Parameters:
    target_list (list of int): The list to which random integers will be appended.
    size (int): The number of random integers to generate.

    Returns:
    None
    """
    for i in range(size):
        random_number = random.randint(1, size)
        target_list.append(random_number)

# Average a list
def f_average_list(list_to_average, average_storage):
    """
    Calculate the average of a list of numbers and store the result.

    Parameters:
    list_to_average (list of float): A list of numbers to average.
    average_storage (list of float): A list where the calculated average will be stored.

    Returns:
    None
    """
    average = sum(list_to_average) / len(list_to_average)
    average = round(average, 1)
    average_storage.append(average)

# # Calculate error rate (currently commented out)
# def f_calculate_error_rate(target_list, error_storage):
#     error_rate = 

# Main Loop
average_list_storage = []
error_rate_list = []
max_number = 10
max_number += 1
for i in range(1, max_number):
    source_list = []
    f_generate_source_list(source_list, i)
    f_average_list(source_list, average_list_storage)
    # f_calculate_error_rate(average_list_storage, error_rate_list)
    print(f"{source_list} = {average_list_storage[-1]} Error Rate = x%")
