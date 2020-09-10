# Name: David Turnbough
# Date: January 8, 2018 Monday
# Geeks for Geeks: Second Largest
# https://practice.geeksforgeeks.org/problems/second-largest/0

def main():
    testCases = int(input())

    while(testCases > 0):
        size = int(input())

        arr = [int(n) for n in input().split()]
                    
        arr.sort()

        print(arr[size - 2])

        testCases = testCases - 1


if __name__ == "__main__":
    main()
