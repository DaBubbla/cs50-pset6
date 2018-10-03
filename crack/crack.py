######################################################
# Program that takes in hashed passwords for crackin #
#                                                    #
######################################################

import sys
import unistd


LETTERS_COUNT = 57

def main():
# One command-line arg ONLY!!
    # Ensure proper usage
    if len(sys.argv) != 2:
        print("Usage: python crack.py <hash>")
        exit(1)

letter = 'a–zA–Z'# OR "\0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
strHash = sys.argv[1]

# chr salt[3]

    # char *crypt(const char *key, const char *salt);
    # salt is a two-character string chosen from the set [a–zA–Z0–9./].

if __name__=='__main__':
    main()