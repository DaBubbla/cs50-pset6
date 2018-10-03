# Determines the least amount of coins needed
# to make the owed change.

from cs50 import get_float

owed = 0.00

while owed < .01:
    owed = get_float("Change owed: ")

n = owed * 100
counter = 0

# Quarters
while n >= 25:
    counter += 1
    n = n - 25

# Dimes
while n >= 10:
    counter += 1
    n = n - 10

# Nickles
while n >= 5:
    counter += 1
    n = n - 5

# Pennies
while n >= 1:
    counter += 1
    n = n - 1

print(counter)