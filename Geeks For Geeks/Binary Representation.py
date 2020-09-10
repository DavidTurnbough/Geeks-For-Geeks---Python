# Name: David Turnbough
# Date: Tuesday December 17, 2019
# https://practice.geeksforgeeks.org/problems/binary-representation/0
# Binary Representation

def convertToBinary(passedValue):
    returnValue = 0

    while(passedValue > 0):
        returnValue = int(returnValue * 10)
        returnValue += int(passedValue % 2)
        passedValue = int(passedValue / 2)
    return returnValue

def main():
    testCases = int(input())

    while(testCases > 0):
        inputValue = int(input())
        outputValue = convertToBinary(inputValue)
        print(outputValue)
        testCases -= 1


if __name__ == '__main__':
    main()
