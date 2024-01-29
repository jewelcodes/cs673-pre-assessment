#!/usr/bin/env python3

# MET CS 673 - Software Engineering
# Programming pre-assessment
# Omar Elghoul
#
# Program that determines if a string is a palindrome

def main():
    while True:
        s = input("Enter a string or 'q' to quit: ")
        if s == 'q':
            exit(0)
        
        if len(s) <= 2:
            print("You need to enter 3 or more characters to test for palindromes.")
        else:
            left = 0
            right = len(s)-1

            for i in range(int(len(s)/2)):
                if s[left] != s[right]:
                    print("The string '" + s + "' is not a palindrome.")
                    break
                
                left += 1
                right -= 1
                if left <= right:
                    print("The string '" + s + "' is a palindrome.")
                    break

if __name__ == "__main__":
    main()
