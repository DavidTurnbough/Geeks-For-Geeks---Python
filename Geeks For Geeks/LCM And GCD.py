# Name: David Turnbough
# Date: Sunday August 12, 2018
# Geeks for Geeks: LCM and GCD
# https://practice.geeksforgeeks.org/problems/lcm-and-gcd/0

def main():
    t = int(input())

    for x in range(t):
        a, b = input().split()
        a = int(a)
        b = int(b)

        lcm = getLCM(a, b)
        gcd = getGCD(a, b)

        print(lcm, gcd)
        
def getLCM(a, b):
    firstValue = int(a)
    secondValue = int(b)
    
    while firstValue != secondValue:
        if firstValue < secondValue:
            firstValue = firstValue + a
        else:
            secondValue = secondValue + b
    return firstValue
    
def getGCD(a, b):
    divisor = int(0)
    x = int(1)

    while x <= min(a, b):
        if a % x == 0 and b % x == 0:
            divisor = x
        x = x + 1
    
    return divisor
    
if __name__ == '__main__':
    main()
