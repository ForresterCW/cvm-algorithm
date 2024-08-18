# Expected-average table
# Avg = N - ((N-1) * 0.5)
length_n = 7
print()
print("N | Average")
print("-----------")
for i in range(1, length_n + 1):
    expected_avg = i - ((i - 1) * 0.5)
    print(f"{i} | {expected_avg}")
print()

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
    float: The average of the numbers in the list, rounded to one decimal place.
    """
    average = sum(list_to_average) / len(list_to_average)
    average = round(average, 1)
    return average

# Calculate error rates
# Error Rate = 1 - ( (Actual Average - Expected Average) / Expected Average) * 100
def f_error_rate_percent(list_to_test):
    """
    Calculate the error rate percentage between the actual average and the expected average for a list.

    Parameters:
    list_to_test (list of float): A list of numbers to test.

    Returns:
    int: The error rate percentage, rounded to the nearest whole number.
    """
    actual_average = f_average_list(list_to_test)
    expected_average = f_expected_average_n(len(list_to_test)) 
    error_rate = abs(actual_average) / abs(expected_average) * 100
    return round(error_rate)

# Testing error rate function
random_numbers = [5, 7, 3, 5, 6, 7, 3]
print(f"{f_error_rate_percent(random_numbers)}%")

# Main Loop (Commented out for future use)
# random_numbers = [5, 7, 3, 5, 6, 7, 3]
# error_rates = []
# print(f_error_rate_percent(random_numbers))
