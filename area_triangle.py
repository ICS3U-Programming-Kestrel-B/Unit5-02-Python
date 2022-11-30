#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 10, 2022
# This program asks how many numbers
# you want to add together, gets that
# numbers of integers from the user,
# and displays the sum

import math


# area function
def calculate_area(height_cm, base_cm):
    try:
        # checking that height_cm is a float
        height_cm_float = float(height_cm)

        # checking that it's bigger than zero
        if height_cm_float > 0:
            try:
                # checking that base_cm is a float
                base_cm_float = float(base_cm)

                # checking that it's bigger than zero
                if base_cm_float > 0:
                    # initializing tri_sum
                    tri_sum = 0.5 * (height_cm_float * base_cm_float)
                    # printing results
                    print("Your area is ", end="")
                    print(tri_sum, end="")
                    print("cm2.")
                else:
                    # negative message
                    print("\n")
                    print("Please enter a positive base.")
            except ValueError:
                # string message
                print("\n")
                print("Please enter a valid base.")
            finally:
                print("\n")
        else:
            # negative message
            print("\n")
            print("Please enter a positive height.")
    except ValueError:
        # string message
        print("\n")
        print(("Please enter a valid height."))
    finally:
        # ending remark
        print("\n")
        print("Thanks for converting!")


def main():
    # introductory paragraph
    print("This program asks how many numbers")
    print("you want to add together, gets that")
    print("numbers of integers from the user,")
    print("and displays the sum")
    print("")

    # input
    # getting height_string
    height_cm = input("Enter the height in cm: ")
    # getting base_string
    base_cm = input("Enter the base in cm: ")

    # calling function
    calculate_area(height_cm, base_cm)


if __name__ == "__main__":
    main()
