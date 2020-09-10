# Name: David Turnbough
# Date: Sunday August 12, 2018
# Geeks for Geeks: Geek and Coffee Shop
# https://practice.geeksforgeeks.org/problems/geek-and-coffee-shop/0

def main():
    testCases = int(input())

    for case in range(testCases):
        units, refills = input().split()
        units = int(units)
        refills = int(refills)

        for refill in range(refills - 1):
            units = units / 2

        print(int(units)) 


if __name__ == '__main__':
    main()
