# Name: David Turnbough
# Date: Sunday August 12, 2018
# Geeks for Geeks: GCD of Two Numbers
# https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers/0

def main():
    testCases = int(input())

    for case in range(testCases):
        a, b = input().split()
        a = int(a)
        b = int(b)

        print(getGCD(a, b))

def getGCD(a, b):
    divisor = min(a, b)

    while divisor >= 1:
        if a % divisor == 0 and b % divisor == 0:
            break
        
        divisor = divisor - 1

    return divisor
    

if __name__ == '__main__':
    main()
