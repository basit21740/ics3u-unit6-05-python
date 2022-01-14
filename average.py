#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program accept marks and calculates the average


def average_calculator(list_of_marks):
    # this functions calculates the average

    average = 0

    for single_element in list_of_marks:
        average = average + single_element

    average = average / len(list_of_marks)
    rounded_average = average * 10 ** 0 + 0.5
    rounded_average = (int(rounded_average)) * 10 ** -0

    return rounded_average


def main():
    # this function uses a list

    mark_list = []
    single_mark = 0

    print("Please enter 1 mark at a time. Enter -1 to end." "\n")

    # input
    while single_mark != "-1":
        single_mark = input("What is your mark? (as %): ")
        try:
            int_single_mark = int(single_mark)

            mark_list.append(int_single_mark)
        except Exception:
            print("Please enter in a number")
            print(" ")

    mark_list.pop()
    print("")

    # call functions
    average = average_calculator(mark_list)
    # output
    print("Your average is: {}% ".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
