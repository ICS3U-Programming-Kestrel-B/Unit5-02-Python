#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 10, 2022
# This program asks how many numbers
# you want to add together, gets that
# numbers of integers from the user,
# and displays the sum

import random
import math


# area function
def calculate_area(height_cm, base_cm):
    try:
        # checking that height_cm is a float
        height_cm_float = float(height_cm)
        print("Test1")
        try:
            # checking that base_cm is a float
            base_cm_float = float(base_cm)

            # doing math stuff
            tri_sum = 0.5 * (height_cm_float * base_cm_float);
            print("2 / (")
            print(height_cm_float);
            print(" * ");
            print(base_cm_float);
            print(" = ");
            print(tri_sum);
            print(")")
        except ValueError:
            print("\n")
            print("Please enter a valid base.")
        finally:
            print("Thanks for converting!2")
    except ValueError:
        print("\n")
        print(("Please enter a valid height."))
    finally:
        print("Thanks for converting!1")

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
