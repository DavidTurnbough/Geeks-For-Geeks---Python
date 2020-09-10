# Name: David Turnbough
# Date: January 9, 2018 Tuesday
# Geeks for Geeks: Check if an Array is Sorted
# https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted/0

def main():
    testCases = int(input())

    while(testCases > 0):
        size = int(input())

        arr = [int(x) for x in input().split()]

        output = int(1)

        for i in range(size - 1):
            if(arr[i] > arr[i + 1]):
                output = int(0)
                break

        print(output)
        
        testCases = testCases - 1


if __name__ == "__main__":
    main()
