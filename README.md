# PYTHON-FUNDAMENTALS-CODECH


## Introduction

This repository contains various utility functions in Python such as sorting, adding and vowel count. Follow the instructions below to set up and use the functions on your local machine.



## Installation

Clone the Repository:

1. Open your terminal and in the directory where you want to install this file, run the following command to clone the repository:
'git@github.com:Ndoria-hubs/python-fundamentals-codech.git'

- Alternatively, use the source link from our repository: 'https://github.com/Ndoria-hubs/python-fundamentals-codech'

2. Navigate to the Directory:

3. Change to the repository directory: '/cd python-fundamentals-codech'

4. Setup Your Environment:

*** Ensure you have Python installed. You can check this by running: 'python--version'
Alternatively, if Python is not installed, download and install it from the official Python website. ***



## How to Run

- Open a Python Interpreter:

You can run Python code in an interpreter or script. To start the interpreter, run: 'python'

- ensure you have created yu have creatde your pwn python file ( filename.py )

- You can import the functions from the lib.py file and use them. For example:

### CODE:
from lib import add_numbers, calculate_factorial

print(add_numbers(5, 3))       # Output: 8
print(calcualte_factorial(5))  # Output: 120
### END OF CODE

To run these functions, execute: 'python filename.py' in your terminal in the parent directory



## Usage

# add_numbers function

***returns the sum of two 2 numbers***

result_add = add_numbers(10, 5)
print(f"Addition Result: {result_add}")  # output = 15

# is_even function 

***checks whether a number is even or odd***

result_check = is_even(4)
print(f"Even Check Result: {result_check}")  # output = True

# calcualte_factorial function

***calculates the factorial of a positive num.The factorial of a non-negative integer n is the product of all positive integers less than or equal to n.***

result_factorial = calcualte_factorial(4)
print(f"Factorial Result: {result_factorial}")  # ooutput = 24

# reverse_string function

***returns a string reversed backword*** 

string_to_reverse = reverse_string('hello')
print(f"Reversed Result: {string_to_reveerse}")  # putput = 'olleh'

# count_vowel function

***Counts the number of vowels in a string***

string_to_count_vowel = count_vowel("Count the vowels in this sentence")
print(f"Vowel_count : {string_to_count_vowel}")  # output = 10

# apply_decorator function

***applies a decorator that prints 'Decorator applied'***

@apply_decorator
def new_function_here():
    # code

new_function_here()   # output: " Decorator applied,
                              (new function result )" 

# sort_by_age

***sorts a tuple list containing a str & num in ascending order according to the num***

input_list = [('John', 20), ('Mary', 16)]
list_sorted = sort_by_age(input_list)
print(f" Result: {list_sorted}")  # output: [('Mary, 16'), ('John', 20)]

# merge_dicts function

***merges 2 dictionaries and adds values for a repeated key***

try_merged_dict = merge_dicts(dictA, dictB)
print(f" Result: {try_merged_dict}")   # output: dictA + dictB

# Car class creation

***Allows user to create a car with attr: model, model, year and display this info***

car1 = Car('Mistubishi','outlander',2017)
car1.display_info()  # output: make : Mistubishi
                               model: outlander
                               year: 2017


### Alternatively:
- Use the example sets under each function to implement and execute teh function as desired!



## Troubleshooting

If you encounter issues with merging or running the code:

- Ensure you are using the latest version of Git.
- Confirm that Python is correctly installed and added to your system’s PATH.
- If merge conflicts arise, resolve them manually as per Git’s instructions.


## Acknowledgements

This project is powered by Samburu Tequees!



## Contact

For questions or feedback, please reach out to us @ kihoto.ndoria@student.moringaschool.com