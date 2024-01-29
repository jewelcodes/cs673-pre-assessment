#!/usr/bin/env python3

# MET CS 673 - Software Engineering
# Programming pre-assessment
# Omar Elghoul
#
# Program that determines if a given year is a leap year

def main():
    # ask the user for input
    while True:
        try:
            s = input("Enter a year or type 'q' to quit: ")
            n = int(s)

            # make sure it's over 1
            if n<1:
                print("The input must be a positive integer.")
            else:
                # leap years are divisible by 4 EXCEPT if they are also divisible by 100;
                # centurial years are leap years ONLY if they are divisible by 400
                if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
                    print("The year " + str(n) + " is a leap year.")
                else:
                    print("The year " + str(n) + " is a common year.")
        except ValueError:      # not a valid integer
            if s == "q":        # to quit
                exit(0)
            else:
                print("'" + s + "' is not a valid integer")

if __name__ == "__main__":
    main()
