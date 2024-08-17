# Expected-average table
## Avg = N - ((N-1) * 0.5)
lengthN = 7
print()
print("N | Average")
print("-----------")
for i in range(1, lengthN+1):
    expectedAvg = i - ((i-1)*0.5)
    print(f"{i} | {expectedAvg}")
print()

# Expected average at a given list size N
## Expected Average = N - ((N-1) * 0.5)
def f_expectedAverageN(valueN):
    expectedAvg = valueN - ((valueN-1)*0.5)
    return expectedAvg

# Average a list
def f_averageList(listToAverage):
    average = sum(listToAverage) / len(listToAverage)
    average = round(average, 1)
    return average

# Calculate error rates
## Error Rate = 1 - (Actual Average / Expected Average) * 100
def f_calcualteErrorRate(numbersToTest, errorRateStorage):
    averageStorage = []
    f_averageList(numbersToTest, averageStorage)
    errorRate = (1 - (averageStorage[-1] / ())) * 100

randomNumbers = [5, 7, 3, 5, 6, 7, 3]
errorRates = []
f_calcualteErrorRate(randomNumbers, errorRates)
print(errorRates)