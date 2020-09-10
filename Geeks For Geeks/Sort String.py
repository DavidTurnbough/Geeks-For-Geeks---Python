# Name: David Turnbough
# Date: January 8, 2018 Monday
# Geeks for Geeks: Sort String
# https://practice.geeksforgeeks.org/problems/sort-string/0

def main():
    testCases = input()
    testCases = int(testCases)

    while (testCases > 0) :
        value = input()

        value = ''.join(sorted(value))

        print(value)

        testCases = (testCases - 1)
        

if __name__ == "__main__":
    main()
