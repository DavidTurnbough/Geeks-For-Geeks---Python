# Name: David Turnbough
# Date: Thursday, December 19, 2019
# Geeks For Geeks: Convert from 12 hour to 24 hour format
# https://practice.geeksforgeeks.org/problems/convert-time-from-12-hour-to-24-hour-format/0

testCase = int(input())

while(testCase > 0):
    testCase -= 1

    TwelveHourFormat = input()

    TwentyFourHourFormat = 0

    hours = TwelveHourFormat[0:2]
    minutes = TwelveHourFormat[3:5]
    seconds = TwelveHourFormat[6:8]
    period = TwelveHourFormat[8:10]

    if(period == 'PM'):
        if(hours == '12'):
            TwentyHourFormat = hours + ':' + minutes + ':' + seconds
        else:
            TwentyHourFormat = str(int(hours) + int(12)) + ':' + minutes + ':' + seconds
    else:
        if(hours == '12'):
            hours = '00'
        TwentyHourFormat = hours + ':' + minutes + ':' + seconds

    print(TwentyHourFormat)
