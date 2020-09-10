# Name: David Turnbough
# Date: Thursday, December 19, 2019
# Geeks For Geeks: Multiples Power
# https://practice.geeksforgeeks.org/problems/multiples-power/0

testCases = int(input())

while(testCases > 0):
    testCases -= 1

    inputValue = int(input())

    total = 0

    index = 1

    while(3*index < inputValue or 7*index < inputValue):
        
        if((3*index) < inputValue):
            total += 3*index
            
        if((7*index) < inputValue):
            total += 7*index

        if((3*7*index) < inputValue):
            total -= (3*7*index)

        index += 1

    print(total)
