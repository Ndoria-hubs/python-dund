
### | 1: add numbers  

def add_numbers(num1, num2):
    sum = num1 + num2  # actual sum 
    return f'1 : {sum}'


#example
example_num1 = 10
example_num2 = 20
print(add_numbers(example_num1, example_num2))





### | 2: check if number is even

def is_even(number):
    # using ternary operator 
    return True if number % 2 == 0 else False


#example
example_num = 20
print(f'2 : {is_even(example_num)}')





### | 3: reverse a string

def reverse_string(string):
    return string[::-1]  # : go to start : go to end : -1 reverse/grab backwards

# example
example_string = 'hello Ndoria'
print(f'3 : {reverse_string(example_string)}')





### | 4: count vowels

def count_vowels(string):
    vowels = 'aeiou'
    count = 0

    # iterate over each character in the string 
    for char in string:
        # check whether is a vowel
        if char in vowels:
            count += 1  # > increment of number of vowels
    return count

# example
example_string2 = 'hello Mr Ndoria'
print(f'4 : {count_vowels(example_string)}')





### | 5: calculate factorial

def calculate_factorial(n):
    if n < 0:
        return "Please insert a positive number"
    else:
        count = 1  # Initialize count to 1
    
    while n > 0:
        count *= n # multiply count by n; e.g- 5 * 1 - so new count = 5
        n -= 1 # subtract n by 1 and (5 - 1 = 4) and redo while loop(multiply)
    return count

# example
print(f'5 : {calculate_factorial(5)}')





### | 6: apply_decorator

def apply_decorator(func):
    def decorator_func():  # >> this is our wrapper(decorator)
        print('>>> Decorator Applied')
        func()
    return decorator_func    # ensure wrapper is returned
        
@apply_decorator
def my_function():
    print(f'6 : Hello Ndoria, decorator applied, exiting decorator...')
my_function()





### | 7: Sequences: Sort List of Tuples

def sort_by_age(tuple_list):
    def grab_age(tuple): # to grab age in tuple <<<<
        return tuple[1] # >> second index of tuple , that is, age
    
    # sort according to age >>>>
    tuple_list.sort(key=grab_age)
    return tuple_list

# example
ages = [('Job', 44), ('Mike', 39), ('John',58), ('Stella', 37), ('Joanne', 29)]
sorted_ages = sort_by_age(ages)
print(f'7 : {sorted_ages}')





### | 8: Merge Dictionaries

def merge_dicts(dict1, dict2):
    new_merged_dict = dict1.copy()  # start with keys & values from the firdt dicitionary

    # new_merged_dict.update(dict2)  #- this would wprk for direct merge but we need to sum values if keys are similar

    # check if there are similar keys
    for key, value in dict2.items():
        # check if key already exists
        if key in new_merged_dict:
            new_merged_dict[key] += value  ## add values if alreayd exist
        else:  
            new_merged_dict[key] =  value # simply add new key if deosn't esxist

    return new_merged_dict

# example
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = merge_dicts(dict1, dict2)
print(f'8 : {result}')





### | 9: Class Creation

class Car:

    # to initialize our car  class  using init
    def __init__(self, make, model, year): 
        self.car_make = make
        self.car_model = model
        self.car_year = year

    # function to display car information
    def display_info(self):
        print(f"""9 :  
            make: {self.car_make}
            model: {self.car_model}
            year: {self.car_year}
            """)
        
# example
car1 = Car('Subaru','Forester',2017)
# implement function
car1.display_info()
