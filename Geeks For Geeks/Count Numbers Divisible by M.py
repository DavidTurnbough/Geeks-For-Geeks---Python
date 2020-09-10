# Name: David Turnbough
# Date: Sunday July 26, 2020
# Geeks For Geeks : Count Numbers Divisible by M
# https://practice.geeksforgeeks.org/problems/count-numbers-divisible-by-m/0

def main():
    
    testCases = int(input())

    while(testCases > 0):

        rawInput = input()

        a, b, m = rawInput.split()

        a = int(a)
        b = int(b)
        m = int(m)

        count = 0

        for i in range(a, b + 1):
            if(i % m == 0):
                count = count + 1
        
        print(count)

        testCases = testCases - 1



if __name__ == '__main__':
    main()
