# Name: David Turnbough
# Date: Sunday July 26, 2020
# Geeks For Geeks: Rectangle Number
## https://practice.geeksforgeeks.org/problems/rectangle-number/0

def main():
    testCases = int(input())

    while(testCases > 0):
        
        height = int(input())
        width = int(input())

        count = int(0)

        area = int(height * width)

        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if(area % (height * width) == 0):
                    print("area = ", area, "height * width = ", i * j)
                    
                    count = int(count + (area / (i * j)))
                    print('Count : ',  count, 'i : ', i, ' j : ', j)
                    
        print(count)

        testCases -= 1


if __name__ == '__main__':
    main()
