# Name: David Turnbough
# Date: Sunday August 12, 2018
# Geeks for Geeks: Split Strings
# https://practice.geeksforgeeks.org/problems/split-strings/0

def main():
    t = int(input())

    for i in range(t):
        s = str(input())

        s1 = ""
        s2 = ""
        s3 = ""

        for j in range(len(s)):
            if s[j].isalpha():
                s1 = s1 + s[j]
            elif s[j].isdigit():
                s2 = s2 + s[j]
            else:
                s3 = s3 + s[j]

        print(s1)
        print(s2)
        print(s3)



if __name__ == '__main__':
    main()
