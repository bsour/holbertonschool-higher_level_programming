# Project README

This project consists of multiple Python programs that demonstrate various concepts related to importing modules and using functions in Python. Each program serves a specific purpose and has its own set of instructions.

## Table of Contents

1. [0. Import a simple function from a simple file](#0-import-a-simple-function-from-a-simple-file)
2. [1. My first toolbox!](#1-my-first-toolbox)
3. [2. How to make a script dynamic!](#2-how-to-make-a-script-dynamic)
4. [3. Infinite addition](#3-infinite-addition)
5. [4. Who are you?](#4-who-are-you)
6. [5. Everything can be imported](#5-everything-can-be-imported)

---

## 0. Import a simple function from a simple file

**Description:** This program imports the function `add(a, b)` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`. The program uses the `print` function with string formatting to display integers. It assigns the value `1` to a variable called `a` and the value `2` to a variable called `b`. These variables are then used as arguments when calling the `add` function and printing the result.

**Instructions:** Run the `0-add.py` file to execute the program. Ensure that the file `add_0.py` is present in the same directory.

Example command:
```
$ python3 0-add.py
```

---

## 1. My first toolbox!

**Description:** This program imports functions from the file `calculator_1.py` and performs mathematical operations using the imported functions. It demonstrates addition, subtraction, multiplication, and division operations using two variables `a` and `b`, which are assigned the values `10` and `5` respectively. The program calls each of the imported functions and prints the results.

**Instructions:** Run the `1-calculation.py` file to execute the program. Ensure that the file `calculator_1.py` is present in the same directory.

Example command:
```
$ python3 1-calculation.py
```

---

## 2. How to make a script dynamic!

**Description:** This program prints the number and list of its command-line arguments. It displays the number of arguments followed by the arguments themselves. The position of each argument is also shown.

**Instructions:** Run the `2-args.py` file to execute the program. Pass command-line arguments as needed.

Example commands:
```
$ python3 2-args.py
$ python3 2-args.py Hello
$ python3 2-args.py Hello Welcome To The Best School
```

---

## 3. Infinite addition

**Description:** This program prints the result of adding all the command-line arguments. It takes any number of arguments and casts them into integers before performing the addition. The result is then printed.

**Instructions:** Run the `3-infinite_add.py` file to execute the program. Pass command-line arguments as needed.

Example commands:
```
$ python3 3-infinite_add.py
$ python3 3-infinite_add.py 79 10
$ python3 3-infinite_add.py 79 10 -40 -300 89
```

---

## 4. Who are you?

**Description:** This program prints all the names defined by the compiled module `hidden_4.pyc`. It prints one name per line, in alphabetical order, excluding names that start with "__".

**Instructions:** Run the `4-hidden_discovery.py` file to execute the program. Make sure the `hidden_4

.pyc` file is present in the same directory. 

Example command:
```
$ python3 4-hidden_discovery.py | sort
```

---

## 5. Everything can be imported

**Description:** This program imports the variable `a` from the file `variable_load_5.py` and prints its value. It demonstrates how to import a specific variable from a module.

**Instructions:** Run the `5-variable_load.py` file to execute the program. Ensure that the file `variable_load_5.py` is present in the same directory.

Example command:
```
$ python3 5-variable_load.py
```

---

**Note:** All the Python files mentioned in the instructions and their corresponding module files should be located in the same directory to ensure proper execution.