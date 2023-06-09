# Project Name

Python More Data Structures - Tasks

## Description

This project contains several Python scripts that implement different functions related to data structures in Python. Each script corresponds to a specific task and has a defined set of requirements and specifications.

## List of Tasks

1. [Squared simple](#squared-simple)
2. [Search and replace](#search-and-replace)
3. [Unique addition](#unique-addition)
4. [Present in both](#present-in-both)
5. [Only differents](#only-differents)
6. [Number of keys](#number-of-keys)
7. [Print sorted dictionary](#print-sorted-dictionary)
8. [Update dictionary](#update-dictionary)
9. [Simple delete by key](#simple-delete-by-key)
10. [Multiply by 2](#multiply-by-2)
11. [Best score](#best-score)
12. [Multiply by using map](#multiply-by-using-map)
13. [Roman to Integer](#roman-to-integer)

## Task Details

### Squared simple

**Description:**

Write a function `square_matrix_simple(matrix=[])` that computes the square value of all integers in a given matrix. The function should return a new matrix with the same size as the input matrix, where each value is the square of the corresponding value in the input matrix. The input matrix should not be modified.

**Prototype:**

```python
def square_matrix_simple(matrix=[]):
```

**Examples:**

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
# Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
print(matrix)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

### Search and replace

**Description:**

Write a function `search_replace(my_list, search, replace)` that replaces all occurrences of an element by another in a new list. The function should take three parameters: `my_list` (the initial list), `search` (the element to replace in the list), and `replace` (the new element). The function should return a new list where all occurrences of `search` in `my_list` are replaced by `replace`. The initial list `my_list` should not be modified.

**Prototype:**

```python
def search_replace(my_list, search, replace):
```

**Examples:**

```python
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
print(new_list)
# Output: [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
print(my_list)
# Output: [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```

### Unique addition

**Description:**

Write a function `uniq_add(my_list=[])` that adds all unique integers in a list, considering each integer only once. The function should return the sum of all the unique integers in the list.

**Prototype:**

```python
def uniq_add(my_list=[]):
```

**Examples:**

```python
my_list
```
