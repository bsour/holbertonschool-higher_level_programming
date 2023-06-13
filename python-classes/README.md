# Square Class

This repository contains the implementation of the `Square` class, which represents a square. The class provides functionality to define, manipulate, and print squares.

## Class Structure

The `Square` class is defined in the `square.py` file.

## Usage

To use the `Square` class, follow the instructions below:

### 0. My First Square

The `Square` class is defined as an empty class without any attributes or methods. It can be instantiated as follows:

```python
my_square = Square()
print(type(my_square))  # Output: <class 'square.Square'>
print(my_square.__dict__)  # Output: {}
```

### 1. Square with Size

The `Square` class has a private instance attribute called `size`. You can instantiate a `Square` object with a specific size:

```python
my_square = Square(3)
print(type(my_square))  # Output: <class 'square.Square'>
print(my_square.__dict__)  # Output: {'_Square__size': 3}
```

### 2. Size Validation

The `Square` class validates the size attribute. It must be an integer and cannot be negative. If an invalid size is provided, an exception will be raised:

```python
my_square_1 = Square(3)
print(type(my_square_1))  # Output: <class 'square.Square'>
print(my_square_1.__dict__)  # Output: {'_Square__size': 3}

my_square_2 = Square()
print(type(my_square_2))  # Output: <class 'square.Square'>
print(my_square_2.__dict__)  # Output: {'_Square__size': 0}

try:
    print(my_square_1.size)  # Raises AttributeError
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)  # Raises AttributeError
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")  # Raises TypeError
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)  # Raises ValueError
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)
```

### 3. Area of a Square

The `Square` class provides a public instance method called `area()`, which returns the current area of the square:

```python
my_square = Square(3)
print("Area: {}".format(my_square.area()))  # Output: Area: 9
```

### 4. Access and Update Private Attribute

The `Square` class has a private instance attribute called `size`. You can access and update this attribute using the `size` property:

```python
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))  # Output: Area: 7921 for size: 89

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))  # Output: Area: 9 for size: 3

try:
    my_square.size = "5 feet"  # Raises TypeError
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
```

### 5. Printing a Square

The `Square` class provides a public instance method called `my_print()`, which prints the square using the `#` character. If the size is 0, an

 empty line is printed:

```python
my_square = Square(3)
my_square.my_print()
# Output:
# ###
# ###
# ###

my_square.size = 10
my_square.my_print()
# Output:
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########
# ##########

my_square.size = 0
my_square.my_print()
# Output:
#
```

### 6. Coordinates of a Square

The `Square` class has an additional private instance attribute called `position`. It represents the top-left position of the square. The position attribute must be a tuple of 2 positive integers. The `my_print()` method takes into account the position when printing the square:

```python
my_square_1 = Square(3)
my_square_1.my_print()
# Output:
# ###
# ###
# ###

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()
# Output:
#  ###
#  ###
#  ###

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()
# Output:
#     ###
#     ###
#     ###
```

## Repository Structure

This repository follows the following structure:

```
├── square.py
└── README.md
```

- `square.py`: Contains the implementation of the `Square` class.
- `README.md`: Provides information and instructions about the `Square` class.

Feel free to explore the repository for more details.

## Contribution

Contributions to the repository are welcome. If you find any issues or would like to add new features, please create a pull request, and we will review it together.

## License

This project is licensed under the MIT License. You can find more information in the [LICENSE](https://github.com/your-username/your-repo/blob/main/LICENSE) file.

We hope you find the `Square` class useful for your projects! If you have any questions, feel free to reach out. Happy coding!