# Name: David Turnbough
# Date: January 9, 2018 Tuesday
# Geeks for Geeks: Check if Array Contains Contiguous Integers with Duplicates Allowed
# https://practice.geeksforgeeks.org/problems/check-if-array-contains-contiguous-integers-with-duplicates-allowed/0

def main():
    testCases = int(input())

    while(testCases > 0):
        size = int(input())
        arr = []

        arr = [int(x) for x in input().split()]

        arr.sort()

        isContiguous = True

        for i in range(size - 1):
            temp = abs(arr[i] - arr[i+1])
            if(temp > 1):
                isContiguous = False
                break


        if(isContiguous):
            print("Yes")
        else:
            print("No")

        testCases = testCases - 1


if __name__ == "__main__":
    main()
