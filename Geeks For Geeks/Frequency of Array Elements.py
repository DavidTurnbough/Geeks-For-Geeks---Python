# Name: David Turnbough
# Date: Sunday August 12, 2018
# Geeks for Geeks: Frequency of Array Elements
# https://practice.geeksforgeeks.org/problems/frequency-of-array-elements/0

def main():   
    testCases = int(input())

    for i in range(testCases):
        size = int(input())

        str_foo = input().split()
        foo = [int(num) for num in str_foo]

        bar = [None] * size

        for j in range(size):
           bar[foo[j]] = bar[foo[j]] + 1

        for j in range(size):
            print(bar[j])

        i = i + 1


if __name__ == '__main__':
    main()

