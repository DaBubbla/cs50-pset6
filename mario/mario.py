# Prints a positive number of question marks as specified
# by user
from cs50 import get_int

# Prompt user to input number
print('Enter a positive int between 1 and 23')
height = get_int('Number: ')

# Only accept user input between 1 and 23
while(height < 0 or height > 23):
    height = get_int('Number: ')

for i in range(height):
    print(" " * (height - (i + 1)) + "#" * (i + 2))
