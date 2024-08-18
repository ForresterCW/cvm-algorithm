# Build a function that can be used to calculate how much the average of a list differs from what we would expect from a linear list of the same values.

# Expected-average table baseline
## Avg = N - ((N-1) * 0.5)
import random


def f_expected_average_table(max_length_to_calculate):
    """
    Display what we expect the averages to be in a linear list up to a length_N.
    
    Parameters:
    length_n (int): The value to count to in the table. 

    Returns: 
    String table of averages.
    """
    print("N | Average")
    print("-----------")
    for i in range(1, max_length_to_calculate + 1):
        expected_avg = i - ((i - 1) * 0.5)
        print(f"{i} | {expected_avg}")


# Expected average at a given list size N
# Expected Average = N - ((N-1) * 0.5)
def f_expected_average_n(value_n):
    """
    Calculate the expected average for a list of a given size N.

    Parameters:
    value_n (int): The size of the list.

    Returns:
    float: The expected average for the list size.
    """
    expected_avg = value_n - ((value_n - 1) * 0.5)
    return expected_avg

# Average a list
def f_average_list(list_to_average):
    """
    Calculate the average of a list of numbers.

    Parameters:
    list_to_average (list of float): A list of numbers to average.

    Returns:
    float: The average of the numbers in the list, rounded to one decimal place, as a percent.
    """
    average = sum(list_to_average) / len(list_to_average)
    average = round(average, 1)
    return average

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

random_numbers = [5, 7, 3, 5, 6, 7, 3]
length_n = 7
# random_numbers = [1]
# length_n = 1
# random_numbers = [5, 7]
# length_n = 2

print()
f_expected_average_table(length_n)
print()
print(f"List = {random_numbers}")
print(f"Expected average = {f_expected_average_n(length_n)}")
print(f"Actual average = {f_average_list(random_numbers)}")
print(f"Error rate = {f_error_rate_percent(random_numbers)}%")
print()
