# To build my version of the CVM algorithm, and explore and visualize the error rates and the impact of the law of large numbers, while comparing it to a baseline simple unique value counting algorithm.

# Importing modules
import random

# Simulating a unique data stream into a source list
sourceList = []
def f_generateSourceList(targetList, size):
    for i in range(size):
        randomNumber = random.randint(1,size)
        targetList.append(randomNumber)
    return


# Algorithm Main Loop
f_generateSourceList(sourceList, 10)
print(sourceList)
