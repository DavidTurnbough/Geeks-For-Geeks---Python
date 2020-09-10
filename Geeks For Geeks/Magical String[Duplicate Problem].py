# Name: David Turnbough
# Date: Sunday August 12, 2018
# Geeks for Geeks: Magical String[Duplicate Problem]
# https://practice.geeksforgeeks.org/problems/magical-string/0

def main():
    testCases = int(input())

    for i in range(testCases):
        inputValue = input()

        outputValue = ""

        for j in range(len(inputValue)):           
            temp = ord(inputValue[j]) - 97
            characterValue = 122 - temp
            outputValue = outputValue + chr(characterValue)

        print(outputValue)


if __name__ == '__main__':
    main()
