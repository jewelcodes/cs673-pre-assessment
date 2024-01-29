#!/usr/bin/env python3

# MET CS 673 - Software Engineering
# Programming pre-assessment
# Omar Elghoul
#
# Program that merges two lists

# parse_list(): parses a string in the format of "[a,b,c]" into an array
# Parameter: list - the string containing the list
# Return: an array containing the individual list items; for example, ["a", "b", "c"]
# Throws: ValueError - if the list is in an incorrect format

def parse_list(s: str):
    if len(s) < 2:
        return None
    
    if s[0] != '[' or s[len(s)-1] != ']':
        raise ValueError("parse_list: invalid list format")

    trimmed = s[1:len(s)-1]     # remove the leading and trailing brackets
    array = trimmed.split(",")

    # remove whitespaces in case there were leading/trailing spaces at the commas
    for i in range(len(array)):
        array[i].strip()

    return array


def main():
    input1 = input("Enter the first list: ")
    input2 = input("Enter the second list: ")

    try:
        list1 = parse_list(input1)
        list2 = parse_list(input2)

        if list1 is None or list2 is None:
            print("You entered an empty list.")
            exit(1)

        if len(list1) != len(list2):
            print("The two lists must be of equal length.")
            exit(1)

        # concatenate the lists in alternating order
        new_list = []
        for i in range(len(list1)):
            new_list.append(list1[i])   # one item from each
            new_list.append(list2[i])

        # now print the new list
        print("Concatenated list: [", end="")
        for i in range(len(new_list)):
            print(new_list[i], end="")
            if i != len(new_list)-1:
                print(",", end="")
        
        print("]")
        exit(0)
    except ValueError:
        print("Invalid list format")
        exit(1)

if __name__ == "__main__":
    main()
