# Name: David Turnbough
# Date: January 9, 2018 Tuesday
# Geeks for Geeks: Print Elements of Array
# https://practice.geeksforgeeks.org/problems/print-elements-of-array/0

def main():
    testCases = int(input())

    while(testCases > 0):
        size = int(input())
        arr = [int(x) for x in input().split()]

        print(*arr)

        testCases = testCases - 1


if __name__ == "__main__":
    main()
