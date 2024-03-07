#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)

        i -= 1
    print("Happy New Year!")    


def square_integers(int_list):
    squared_numbers = []
    for number in int_list:
        squared_number = number ** 2
        squared_numbers.append(squared_number)
    return squared_numbers
    

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    
