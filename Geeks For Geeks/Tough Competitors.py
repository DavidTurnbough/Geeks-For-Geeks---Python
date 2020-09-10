def main():
    testCases = input();

    for case in range(int(testCases)):
        arr = list();
        size = raw_input();

        for i in range(int(size)):
            n = raw_input();
            arr.append(int(n));

        arr.sort();
        
        skills = 999999;

        for i in range((int(size) - 1)):
            temp = abs(arr[i] - arr[i + 1]);
            if(temp < skills):
                skills = temp;
            
        print(skills);

if __name__ == "__main__":
    main()
