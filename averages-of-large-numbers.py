# Goal: To see how the average changes as the number of random numbers increases.
## Prediction: As random numbers -> inf, avg / (source list /2) = 1

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
    average = round(average, 1)
    averageStorage.append(average)

# # f_calculateErrorRate()
# def f_calculateErrorRate(targetList,errorStorage):
#     errorRate = 

# Main Loop
averageList = []
errorRateList = []
maxNumber = 10
maxNumber += 1
for i in range(1,maxNumber):
    sourceList = []
    f_generateSourceList(sourceList, i)
    f_averageList(sourceList, averageList)
    # f_calculateErrorRate(averageList, errorRateList)
    print(f"{sourceList} = {averageList[-1]} Error Rate = x%")
