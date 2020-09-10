# Name: David Turnbough
# Date: Monday August 13, 2018
# Geeks for Geeks: Compute (a*b)%c
# https://practice.geeksforgeeks.org/problems/compute-abc/0

def main():
    testCases = int(input())

    for case in range(testCases):
        a, b, c = input().split()
        a = int(a)
        b = int(b)
        c = int(c)

        print((a*b)%c)


if __name__ == '__main__':
    main()
