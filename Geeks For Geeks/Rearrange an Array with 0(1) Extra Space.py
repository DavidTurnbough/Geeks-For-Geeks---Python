# Name: David Turnbough
# Date: Sunday August 12, 2018
# Geeks for Geeks: Rearrange an Array with 0(1) Extra Space
# https://practice.geeksforgeeks.org/problems/rearrange-an-array-with-o1-extra-space/0

def main():
    testCases = int(input())

    for case in range(testCases):
        size = int(input())

        str_arr = input().split()
        arr = [int(index) for index in str_arr]

        arr.sort()

        for index in range(size):
            print(arr[index])


if __name__ == '__main__':
    main()
