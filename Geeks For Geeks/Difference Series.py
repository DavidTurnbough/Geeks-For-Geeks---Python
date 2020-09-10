# Name: David Turnbough
# Date: Monday August 13, 2018
# Geeks for Geeks: Difference Series
# https://practice.geeksforgeeks.org/problems/difference-series/0

testCases = int(input())

for case in range(testCases):
    x = int(input())
    print(2 * (x * x) + x)
