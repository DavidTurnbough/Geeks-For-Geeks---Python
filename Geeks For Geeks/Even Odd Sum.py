# Name: David Turnbough
# Date: Monday August 13,2018
# Geeks for Geeks: Even Odd Sum
# https://practice.geeksforgeeks.org/problems/even-odd-sum/0

def main():
    testCases = int(input())

    for case in range(testCases):
        size = int(input())
        arr_str = input().split()
        arr = [int(element) for element in arr_str]

        odd = int(0)
        even = int(0)

        for index in range(size):
            if index % 2 == 0:
                odd = odd + arr[index]
            else:
                even = even + arr[index]
        
        print(odd)
        print(even)


if __name__ == '__main__':
    main()
