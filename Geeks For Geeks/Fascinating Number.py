# Name: David Turnbough
# Date: Thursday, December 19, 2019
# Geeks For Geeks: Fascinating Number
# https://practice.geeksforgeeks.org/problems/fascinating-number/0

testCases = int(input())

while(testCases > 0):
    testCases -= 1

    inputValue = int(input())

    if(len(str(inputValue)) >= 3):

        doubleInputValue = inputValue * 2
        tripleInputValue = inputValue * 3

        inputValue = str(inputValue) + str(doubleInputValue) + str(tripleInputValue)

        valueFound = False
        
        for i in range(1, 10):
            valueFound = False
            index = 0

            while(index < len(inputValue) and valueFound == False):

                if(str(i) == inputValue[index]):
                    valueFound = True

                index += 1

            if(valueFound == False):
                break
                
        if(valueFound == False):
            outputValue = 'Not Fascinating'
        else:
            outputValue = 'Fascinating'
            
    else:
        outputValue = 'Number should be atleast three digits'
    print(outputValue)
