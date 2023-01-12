#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    
    print("Happy New Year!")

def square_integers(int_list):
    int_list = [i * i for i in int_list]
    return int_list
    # square_integers = []
    # for i in int_list:
    #     squared = i * i
    #     square_integers.append(squared)
    # return square_integers

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
    
