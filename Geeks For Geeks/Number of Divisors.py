# Name: David Turnbough
# Date: Thursday, December 19, 2019
# Geeks For Geeks: Number Of Divisors
# https://practice.geeksforgeeks.org/problems/number-of-divisors/0

testCases = int(input())

while(testCases > 0):
    testCases -= 1

    inputValue = int(input())

    total = 0

    divisor = 1

    while(divisor <= inputValue):
        if(inputValue % divisor == 0 and divisor % 3 == 0):
            total += 1
        divisor += 1

    print(total)
