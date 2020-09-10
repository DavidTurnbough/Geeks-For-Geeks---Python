# Name: David Turnbough
# Date: January 13, 2018 Saturday
# Geeks for Geeks: Greatest of Three Numbers
# https://practice.geeksforgeeks.org/problems/greatest-of-three-numbers/0/?ref=self

def main():
    testCases = int(input())

    while(testCases > 0):
        values = input()
        values = values.split(' ')

        firstValue = int(values[0])
        secondValue = int(values[1])
        thirdValue = int(values[2])

        

        largestValue = firstValue if firstValue >= secondValue else secondValue
        largestValue = largestValue if largestValue >= thirdValue else thirdValue

        print(largestValue)


        testCases = testCases - 1

if __name__ == "__main__":
    main()
