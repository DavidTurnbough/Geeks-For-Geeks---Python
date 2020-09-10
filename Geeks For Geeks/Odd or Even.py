# Name: David Turnbough
# Date: January 13, 2018 Saturday
# Geeks for Geeks: Odd or Even
# https://practice.geeksforgeeks.org/problems/odd-or-even/0

def main():
    testCases = int(input())

    while(testCases > 0):
        value = int(input())
        
        if (value % 2 == 0):
            print("even")
        else:
            print("odd")

        testCases = testCases - 1


if __name__ == "__main__":
    main()
