# Name: David Turnbough
# Date: Tuesday July 28, 2020
# Geeks For Geeks : Required Rooms
# https://practice.geeksforgeeks.org/problems/required-rooms/0

import math as math

testCases = int(input())

while(testCases > 0):
    inputValue = input()
    
    foreign, indian = map(int, inputValue.split())

    smallestGroup = math.gcd(foreign, indian)

    numberOfRooms = foreign // smallestGroup + indian // smallestGroup

    print(numberOfRooms)

    testCases -= 1
