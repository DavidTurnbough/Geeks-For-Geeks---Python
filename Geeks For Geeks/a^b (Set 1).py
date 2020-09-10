# Name: David Turnbough
# Date: January 13, 2018 Saturday
# Geeks for Geeks: a^b (set 1)
# https://practice.geeksforgeeks.org/problems/ab-set-1/0/?ref=self

def main():
    testCases = int(input())

    while(testCases > 0):
        userInput = input()
        userInput = userInput.split(' ')
        
        base = int(userInput[0])
        power = int(userInput[1])
        total = int(1)

        for i in range(power):
            total = total * base

        print(total)    

        testCases = testCases - 1
    

if __name__ == "__main__":
    main()
