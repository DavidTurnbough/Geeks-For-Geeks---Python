def main():
    testCases = int(input());

    while(testCases > 0):
        size = int(input());

        arr = [];

        for i in range(size):
            arr.append(input());

        key = input();

        left = 0;
        right = (size - 1);

        while (left < size):
            if(arr[left] == key):
                break;
            left = left + 1;

        while(right > 0):
            if(arr[right] == key):
                break;
            right = right - 1;

        print("{} {}".format(left, right));

        testCases = testCases - 1;
    


if __name__ == "__main__":
    main();
