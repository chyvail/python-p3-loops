#!/usr/bin/env python3

import ipdb

def happy_new_year():
    # code goes here!
    i = 10
    while i <= 10:
        print(i)
        if(i == 1):
            print("Happy New Year!")
            break
        else:
            i-=1

def square_integers(int_list):
    # code goes here!
    new_list = list()
    for i in int_list:
        indiv_item = i**2
        new_list.append(indiv_item)
    return new_list

def fizzbuzz():
    # code goes here!
    i = 0
    while i < 100:
        i+=1
        if(i%3 == 0 and i%5 == 0):
            print("FizzBuzz")
        elif(i%3 == 0):
            print("Fizz")
        elif(i%5 == 0):
            print("Buzz")
        else:
            print(i)
