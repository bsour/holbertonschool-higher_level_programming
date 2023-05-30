# Python Scripts

This repository contains Python scripts for various tasks. The scripts are written to be executed on Ubuntu 20.04 LTS using Python 3.8.*. All files should end with a new line and the first line of each file should be exactly `#!/usr/bin/python3`.

## Installation and Setup
To use these scripts, follow the instructions below:

1. Clone the repository: [holbertonschool-higher_level_programming](https://github.com/holbertonschool-higher_level_programming).
2. Navigate to the `python-hello_world` directory.

## Dependencies
The scripts in this repository require the following dependencies:

- `pycodestyle` (version 2.7.*) - Pycodestyle is the new standard for Python style code.

You can install `pycodestyle` using the following command:
```
pip install pycodestyle==2.7.*
```

## Usage
Each script in this repository serves a specific task. Below is a description of each script and how to use it:

### 0. Hello, print (`2-print.py`)
This script prints the string "Programming is like building a multilingual puzzle" followed by a new line.

To run the script:
```
./2-print.py
```

### 1. Print integer (`3-print_number.py`)
This script prints the integer stored in the variable `number`, followed by the string "Battery street" and a new line. It uses f-strings for formatting and does not cast the variable `number` into a string.

To run the script:
```
./3-print_number.py
```

### 2. Print float (`4-print_float.py`)
This script prints the float stored in the variable `number` with a precision of 2 digits. The output includes the string "Float:" followed by the formatted float and a new line.

To run the script:
```
./4-print_float.py
```

### 3. Print string (`5-print_string.py`)
This script prints the value of the variable `str` three times, followed by its first 9 characters. The output is separated by new lines.

To run the script:
```
./5-print_string.py
```

### 4. Play with strings (`6-concat.py`)
This script prints the string "Welcome to Holberton School!" using the variables `str1` and `str2`. It does not use any loops or conditional statements.

To run the script:
```
./6-concat.py
```

### 5. Copy - Cut - Paste (`7-edges.py`)
This script manipulates the variable `word` and creates three new variables: `word_first_3` containing the first 3 letters of `word`, `word_last_2` containing the last 2 letters of `word`, and `middle_word` containing the value of `word` without the first and last letters. The script does not use any loops or conditional statements.

To run the script:
```
./7-edges.py
```

### 6. Create a new sentence (`8-concat_edges.py`)
This script prints the string "object-oriented programming with Python" using the given code. It does not use any loops or conditional statements, and the program is exactly 5 lines long.

To run the script:
```
./8-concat_edges.py
```

### 7. Easter Egg (`9-easter_egg.py`)
This script prints "The Zen of Python" by Tim Peters, along with the entire Zen of Python text. The script is limited to a maximum of 98 characters in length.

To run the script:
```
./9-easter_egg.py
```

Please refer to the individual script files

 for more details and specific implementation.

## License
This repository is licensed under the [MIT License](LICENSE).

Feel free to explore and use the scripts according to your needs. Contributions and improvements are welcome!