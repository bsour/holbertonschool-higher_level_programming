#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = number_str[-1]

str_1 = "Last digit of"
str_2 = "is"
str_greater_than_5 = "and is greater than 5"
str_is_0 = "and is 0"
str_less_than_6_not_0 = "and is less than 6 and not 0"

if int(last_digit) > 5:
    print(f"{str_1} {number_str} {str_2} {last_digit} {str_greater_than_5}")
elif int(last_digit) == 0:
    print(f"{str_1} {number_str} {str_2} {last_digit} {str_is_0}")
elif int(last_digit) < 6 and int(last_digit) != 0:
    print(f"{str_1} {number_str} {str_2} {last_digit} {str_less_than_6_not_0}")
