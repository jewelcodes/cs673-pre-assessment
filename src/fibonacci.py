#!/usr/bin/env python3

# MET CS 673 - Software Engineering
# Programming pre-assessment
# Omar Elghoul
#
# Program that prints the first 100 Fibonacci numbers

sequence = []   # we will store already computed values here to save time

# fibonacci(): recursively compute the n-th Fibonacci number without re-computing previously-computed values
# Parameter: n - a non-negative integer (zero-based)
# Return: the Fibonacci number at this index
# Throws: ValueError - if n is a negative number

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci: n value must be non-negative")
    elif n == 0 or n == 1:
        output = 1
    elif len(sequence) >= n:
        return sequence[n-1]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
    
    # save the computed values to save time
    if len(sequence) == (n-1):
        sequence.append(output)

    return output


def main():
    for i in range(100):
        print(str(i+1) + ": " + str(fibonacci(i)))

if __name__ == "__main__":
    main()
