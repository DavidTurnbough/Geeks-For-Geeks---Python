# Name: David Turnbough
# Date: Sunday August 12, 2018
# Geeks for Geeks : Number of Factors
# https://practice.geeksforgeeks.org/problems/number-of-factors/0

def main():
    
    testCases = int(input())

    for x in range(testCases):
        inputValue = int(input())

        total = int(0)
        i = int(1);

        while i <= inputValue:
            if inputValue % i == 0:
                total = total + 1
            i = i + 1
                
        print(total)
    

if __name__ == "__main__":
    main()
