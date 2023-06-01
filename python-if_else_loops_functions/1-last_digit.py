#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

str_1 = "Last digit of"
str_2 = "is"
str_greater_than_5 = "and is greater than 5"
str_is_0 = "and is 0"
str_less_than_6_not_0 = "and is less than 6 and not 0"

if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    print(f"{str_1} {number} {str_2} {last_digit} {str_greater_than_5}")
elif last_digit == 0:
    print(f"{str_1} {number} {str_2} {last_digit} {str_is_0}")
else:
    print(f"{str_1} {number} {str_2} {last_digit} {str_less_than_6_not_0}")
