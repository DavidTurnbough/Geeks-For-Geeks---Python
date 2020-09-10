# Name: David Turnbough
# Date: January 9, 2018 Tuesday
# Geeks for Geeks: Cyclically Rotate an Array by One
# https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one/0

def main():
    testCases = int(input())

    while(testCases > 0):
        size = int(input())

        arr = []

        arr = [int(x) for x in input().split()]

        temp = int(arr[size - 1])

        i = int(size - 2)

        while i >= 0:
            arr[i + 1] = arr[i]
            i = i - 1

        arr[0] = temp

        print(*arr)

        testCases = testCases - 1


if __name__ == "__main__":
    main()
