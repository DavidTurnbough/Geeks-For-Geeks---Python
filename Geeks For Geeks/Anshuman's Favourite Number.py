# Name: David Turnbough
# Date: Monday August 13, 2018
# Geeks for Geeks: Anshuman's Favourite Number
# https://practice.geeksforgeeks.org/problems/anshumans-favourite-number/0

testCases = int(input())

for case in range(testCases):
    value = int(input())
    if value % 5 == 0:
        print('YES')
    else:
        print('NO')
