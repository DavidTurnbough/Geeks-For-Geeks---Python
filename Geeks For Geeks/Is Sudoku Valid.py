# Name: David Turnbough
# Date: Tuesday July 28, 2020
# Geeks For Geeks: Is Sudoku Valid
# https://practice.geeksforgeeks.org/problems/is-sudoku-valid/0



testCases = int(intput())

while(testCases > 0):

    rowSize = int(3)
    colSize = int(3)

    mat = [[0 for x in range(rowSize)] for y in range(colSize)]

    

    testCases -= 1
