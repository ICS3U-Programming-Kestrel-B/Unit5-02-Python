#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 10, 2022
# This program asks how many numbers
# you want to add together, gets that
# numbers of integers from the user,
# and displays the sum

import random
import math


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
    base_cm = input("Enter the base in cm:")

    # area function
    def calculate_area(height_cm, base_cm):
        # checking that height_cm is a float
        try:
            height_cm_float = float(height_cm)
        except ValueError:
            print("\n")
            print(("Please enter a valid height."))
        finally:
            print("Thanks for converting!")


if __name__ == "__main__":
    main()
