#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 14, 2021
# This program generates 10 random numbers then
# it calculates the average of them

# import the necessary modules
import random
import const


# greet the user
def greet():
    print("Welcome! This program generates 10 random numbers and will then \
determine the largest, and smallest of those numbers")


# finds the smallest number
def smallest(array):
    min_num = 100
    for each in array:
        if (each < min_num):
            min_num = each
    return min_num


# finds the biggest number
def largest(array):
    max_num = 0
    for each in array:
        if (each > max_num):
            max_num = each

    return max_num


# main function
def main():
    # initialize the list
    array_of_nums = []
    # generate 10 random numbers and add them to the list
    for each in range(0, const.NUM_NUMS):
        array_of_nums.append(random.randint(const.MIN, const.MAX))

    # calls the functions and saves the results
    min_num = smallest(array_of_nums)
    max_num = largest(array_of_nums)

    # print all these things back to the user
    print(array_of_nums)
    print("The largest of these numbers is {}".format(max_num))
    print("The smallest of these numbers is {}".format(min_num))


# gets the program started
if __name__ == "__main__":
    greet()
    main()
