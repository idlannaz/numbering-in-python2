# Numbering-in-python2

Welcome to my Python code collection! This repository contains several simple Python scripts that demonstrate basic programming concepts such as functions, user input, list manipulation, and control flow. These scripts are great for beginners looking to understand the fundamentals of Python programming.

## Table of Contents

- [Getting Started](#getting-started)
- [Scripts Overview](#scripts-overview)
  - [Greeting Users](#greeting-users)
  - [Summing Numbers](#summing-numbers)
  - [List Manipulation](#list-manipulation)
  - [Control Flow Examples](#control-flow-examples)
    - [Breaking a Loop](#breaking-a-loop)
    - [Continuing a Loop](#continuing-a-loop)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Getting Started

To run these scripts, you need to have Python installed on your system. You can download the latest version of Python from the [official website](https://www.python.org/downloads/).

Clone this repository to your local machine using:

```bash
git clone https://github.com/yourusername/your-repository-name.git
```

Navigate to the cloned directory:

```bash
cd your-repository-name
```

---

## Scripts Overview

### Greeting Users

#### 1. Simple Greeting

**File:** `greet_user_simple.py`

**Description:**
This script prompts the user to enter their name and then greets them with a welcome message.

**Code:**
```python
def greet_user(name):
    print(f"Hello, {name}! Welcome!")

name = input("Enter your name: ")
greet_user(name)
```

**Usage:**
Run the script, enter your name when prompted, and receive a personalized greeting.

**Example Output:**
```
Enter your name: Alice
Hello, Alice! Welcome!
```

#### 2. Advanced Greeting

**File:** `greet_user_advanced.py`

**Description:**
An enhanced version of the greeting script that includes a default greeting and name if none are provided.

**Code:**
```python
def greet_user(name, greeting="Ohaiyo"):
    if not name:
        name = "Dumkopf"
    print(f"{greeting}, {name}! Welcome!")

name = input("Enter your name: ")
greet_user(name)
```

**Usage:**
Run the script and enter your name. If no name is entered, it uses the default name "Dumkopf" and the default greeting "Ohaiyo".

**Example Output:**
```
Enter your name: 
Ohaiyo, Dumkopf! Welcome!
```

---

### Summing Numbers

**File:** `sum_numbers.py`

**Description:**
This script takes two numbers as input from the user, sums them using a function, and displays the result.

**Code:**
```python
def sum_numbers(a, b):
    return a + b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

result = sum_numbers(a, b)

print("The sum is:", result)
```

**Usage:**
Run the script and enter two numbers when prompted to receive their sum.

**Example Output:**
```
Enter the first number: 5
Enter the second number: 10
The sum is: 15
```

---

### List Manipulation

**File:** `fruits_list.py`

**Description:**
This script demonstrates various list operations such as appending, removing, inserting, and sorting elements in a list.

**Code:**
```python
fruits = ["apple", "banana", "cherry", "date"]

fruits.append("elderberry")  # Add "elderberry" to the end of the list

fruits.remove("banana")  # Remove "banana" from the list

fruits.insert(1, "blueberry")  # Insert "blueberry" at the second position in the list

fruits.sort()  # Sort the list in alphabetical order

print(fruits)  # Output the modified list
```

**Usage:**
Run the script to see the sequence of list manipulations and the final sorted list.

**Example Output:**
```
['apple', 'blueberry', 'cherry', 'date', 'elderberry']
```

---

### Control Flow Examples

#### 1. Breaking a Loop

**File:** `break_loop.py`

**Description:**
This script uses a `for` loop to print numbers from 1 to 10 but breaks the loop when the number reaches 7.

**Code:**
```python
for num in range(1, 11):
    print(num)
    if num == 7:
        break
```

**Usage:**
Run the script to see numbers printed from 1 up to 7.

**Example Output:**
```
1
2
3
4
5
6
7
```

#### 2. Continuing a Loop

**File:** `continue_loop.py`

**Description:**
This script uses a `for` loop to print numbers from 1 to 10, skipping numbers that are divisible by 3.

**Code:**
```python
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num)
```

**Usage:**
Run the script to see numbers from 1 to 10 excluding those divisible by 3.

**Example Output:**
```
1
2
4
5
7
8
10
```

---

## Requirements

- Python 3.x
- No additional libraries or dependencies are required.

---

## Usage

1. Ensure you have Python 3 installed on your system.
2. Clone the repository to your local machine.
3. Navigate to the directory containing the scripts.
4. Run the desired script using the command:

```bash
python script_name.py
```

**Example:**
```bash
python greet_user_simple.py
```

---

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.

**Steps to Contribute:**

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch to your fork.
4. Create a pull request detailing your changes.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this code as per the terms of the license.

---

**Author:** [IdlanNaz](https://github.com/idlannaz)

**Contact:** idlanmohd01@gmail.com 

---

*Thank you for checking out my Python code collection! I hope these examples help you understand basic Python programming concepts. Happy coding!*