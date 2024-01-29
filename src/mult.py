#!/usr/bin/env python3

# MET CS 673 - Software Engineering
# Programming pre-assessment
# Omar Elghoul
#
# Program that prints the multiplication tables of numbers up to 12

def main():
    # print the multiplication tables in a matrix-like format
    # columns header
    print("  *  ", end="")
    for i in range(12):
        print(str(i+1).ljust(3), end=" ")

    print()

    # row headers and actual values
    for i in range(12):
        print(str(i+1).rjust(3), end="  ")

        for j in range(12):
            print(str((i+1)*(j+1)).ljust(3), end=" ")

        print()

if __name__ == "__main__":
    main()
