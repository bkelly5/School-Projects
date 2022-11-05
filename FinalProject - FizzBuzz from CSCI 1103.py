#Author: Brenden Kelly
#Date: 8/9/2021
#FileName: FinalProject.py
#Program description: This program accepts 2 numbers from the user and outputs
#every number in the range between the inputted values. If any value is evenly
#divisible by 3, 5, or both, the program will display that result next to the value.

test='nothing'

def fizzbuzz():
    global first
    global second
    second = second + 1
    for x in range(first,second):
        if x%3==0 and x%5==0:
            print(x,'is evenly divisible by both 3 & 5')
        elif x%3==0:
            print(x,'is evenly divisible by 3')
        elif x%5==0:
            print(x,'is evenly divisible by 5')
        else:
            print(x)

while test=='nothing':
    first=input('Please enter the starting number: ')
    second=input('Please enter the ending number: ')
    try:
        int(first)
        int(second)
    except:
        test='nothing'
        print('\nIncorrect input\n')
    else:
        first=int(first)
        second=int(second)
        fizzbuzz()
        test='done'
