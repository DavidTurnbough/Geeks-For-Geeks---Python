# Name: David Turnbough
# Date: Monday July 27, 2020
# Geeks For Geeks: Number Following A Pattern
# https://practice.geeksforgeeks.org/problems/number-following-a-pattern/0

testCases = int(input())

while(testCases > 0):

    rawInput = input()

    outputValue = [1] * int(len(rawInput) + 1)
                  
    for i in range(len(rawInput)):
        if(rawInput[i] == 'D'):
            for j in range(i+1):
                outputValue[j+1] = outputValue[j] - 1
        elif(rawInput[i] == 'I'):
            for j in range(i+1):
                outputValue[j+1] = outputValue[j] + 1

    for i in range(len(rawInput) + 1):
        print(outputValue[i] , ' ')

    testCases = testCases - 1
