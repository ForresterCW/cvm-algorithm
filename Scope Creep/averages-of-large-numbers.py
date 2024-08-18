# Goal: To see how the average changes as the number of random numbers increases.
## Prediction: As random numbers -> inf, the average of the list should approach the midpoint of that linear list N
## Prediction: As random numbers -> inf, avg / (source list / 2) = 1

import random

# Return a list of random numbers
def f_generate_source_list(size):
    """
    Generate a list of random integers and append them to the target list.

    Parameters:
    size (int): The number of random integers to generate.

    Returns:
    List of random integers
    """
    randomList = []
    for i in range(1, size + 1):
        random_number = random.randint(1, size)
        randomList.append(random_number)
    return randomList

# Calculate error rates
## Error Rate % = 1 - (( (Actual Average - Expected Average) / Expected Average) * 100) + 100
def f_error_rate_percent(list_to_test):
    """
    Calculate the error rate percentage between the actual average and the expected average for a list.

    Parameters:
    list_to_test (list of float): A list of numbers to test.

    Returns:
    int: The error rate percentage, rounded to the nearest whole number.
    """
    # Calculate the actual average
    actual_average = sum(list_to_test) / len(list_to_test)
    actual_average = round(actual_average, 1)

    # Calculate the expected average based on the length of the list
    value_n = len(list_to_test)
    expected_average = value_n - ((value_n - 1) * 0.5)

    # Calculate the error rate
    error_rate = (1 - (abs(actual_average) / abs(expected_average))) * -100
    return round(error_rate)


# Main Loop
for i in range(1, 6):  # Generates lists with sizes from 1 to 5
    print(f_generate_source_list(i))
