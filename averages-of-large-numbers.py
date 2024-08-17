# Goal: To see how the average changes as the number of random numbers increases.
## Prediction: As random numbers -> inf, avg / (source list /2) = 1

# Importing modules
import random

# Simulate a unique data stream into a source list
def f_generateSourceList(targetList, size):
    for i in range(size):
        randomNumber = random.randint(1,size)
        targetList.append(randomNumber)
    return

# Average a list
def f_averageList(listToAverage, averageStorage):
    average = sum(listToAverage) / len(listToAverage)
    round(average, 1)
    averageStorage.append(average)


# Main Loop
randomAverages = []

for i in range(1,11):
    sourceList = []
    f_generateSourceList(sourceList, i)
    print(sourceList)
    f_averageList(sourceList, randomAverages)
    print(f"List {i} average = {randomAverages[-1]}")