# Single function: Flip a coin, return true/false

from random import randint, random

probability_factor = 0.5
probability_scaling_factor = 0.5

true = 0
false = 0

for i in range(1000000):
    if random() <= probability_factor:
        true += 1
    else:
        false += 1

print(true)
print(false)

print(true / false / 2)


# TODO Useable
if random() <= probability_factor:
    true += 1
else:
    false += 1
