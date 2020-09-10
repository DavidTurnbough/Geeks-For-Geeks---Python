# Name: David Turnbough
# Date: January 9, 2018 Tuesday
# Geeks for Geeks: Average
# https://practice.geeksforgeeks.org/problems/average/0

def main():
    testCases = int(input())

    while(testCases > 0):
        size = int(input())
        arr = [int(x) for x in input().split()]
        avg = []

        runningTotal = int(0)
        count = int(0)

        for i in range(size):
            runningTotal = runningTotal + arr[i]
            count = i + 1
            avg.append(int(runningTotal / count))

        print(*avg)
        
        testCases = testCases - 1


if __name__ == "__main__":
    main()
