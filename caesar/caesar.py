################################################################
#                       Caesar's cipher                        #
# Takes a string, input by the user, as well as a key value    #
# and outputs a new message based on shifting the ascii values #
#                                                              #
################################################################

import sys
from cs50 import get_string

def main():

    # Ensure proper usage
    if len(sys.argv) != 2:
        print("Usage: python caesar.py [number]")
        exit(1)

    # Key storage
    key = int(sys.argv[1])

    # Get string from user
    plaintext = get_string("Plaintext: ")
    print("ciphertext: ", end='')

    for i in range(len(plaintext)):
        # If char is UPPERCASE
        if str.isupper(plaintext[i]):
            upper = (((ord(plaintext[i]) - 65) + key) % 26) + 65
            print(chr(upper), end='')
        # If char is LOWERCASE
        elif str.islower(plaintext[i]):
            lower = (((ord(plaintext[i]) - 97) + key) % 26) + 97
            print(chr(lower), end='')
        # else PRINT IT!
        else:
            print("{}".format(plaintext[i]), end='')

    # Print a new line
    print()

if __name__=="__main__":
    main()