#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: Feb. 14, 2025
# This program does basic math.

import math


def main():

    # Stores a table of tuples that include the string and literal versions of the expressions.
    operations_table = [
        ("2 + 3", 2 + 3),  # Addition.
        ("5 - 4", 5 - 4),  # Subtraction.
        ("7 * 6", 7 * 6),  # Multiplication.
        ("8 / 3", 8 / 3),  # Division.
        ("3 ** 2", 3 ** 2),  # Exponentiation (Powers).
        ("\u221a4", math.sqrt(4)),  # Square Root.
        ("99 % 8", 99 % 8),  # Modulo.
    ]

    # For loop to iterate the elements of the table, where i[0] and i[1] are the first and second elements of the tuple, respectively.
    for i in operations_table:
        print(i[0] + " = {} ".format(i[1]))


if __name__ == "__main__":
    main()
