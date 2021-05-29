#!/usr/bin/env python3

# Created by: Hussein Mansour
# Created on: Fri/May28/2021
# This program calculates the volume of rectangular prism


def volume_rectangular(length_int, width_int, height_int):
    # this function calculates the volume of rectangular prism using return
    # process
    volume = length_int * width_int * height_int
    # return
    return volume


def main():
    # this function this function call other functions
    # input
    print("To calculate the volume of rectangular prism:")
    length_from_user = input("Enter the length (cm): ")
    width_from_user = input("Enter the width (cm): ")
    height_from_user = input("Enter the height (cm): ")
    try:
        length_int = int(length_from_user)
        width_int = int(width_from_user)
        height_int = int(height_from_user)
        # call function
        volume_rectangular(length_int, width_int, height_int)
        # output
        print(
            "\nvolume = {0}cm³"
            .format(volume_rectangular(length_int, width_int, height_int)))
    except Exception:
        print("\nInvalid Input!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
