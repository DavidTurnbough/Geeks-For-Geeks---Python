# Name: David Turnbough
# Date: Thursday, December 19, 2019
# Geeks For Geeks: Count Digits
# https://practice.geeksforgeeks.org/problems/count-digits/0

testCases = int(input())

while(testCases > 0):
    testCases -= 1

    inputValue = int(input())

    total = 0

    tempInputValue = inputValue

    while(tempInputValue > 0):
        divisor = int(tempInputValue % 10)
        tempInputValue = int(tempInputValue / 10)

        if(divisor != 0 and inputValue % divisor == 0):
            total += 1
        
    print(total)    
