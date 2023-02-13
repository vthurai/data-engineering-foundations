import datetime

### String Manipulation
## 1. Remove the second character 'a' from any of the strings passed into the function and return the result.
## For example, 'banana' should be return as 'banna'

def return_new_string_simple(name: str):
    return None # Change the code inside this function

assert(return_new_string_simple('banana') == 'banna')
assert(return_new_string_simple('aaa') == 'aa')
assert(return_new_string_simple('pineapplepan') == 'pineapplepn')
assert(return_new_string_simple('mississauga') == 'mississaug')
assert(return_new_string_simple('paper') == 'paper')

## 2. Using the above written code, modify the code so the user can input the character they want to drop
## and the at which occurance
## E.g. Drop the 3rd 'i' in mississipi --> mississpi

def return_new_string_complex(name: str, char: str, occurance: int):
    return None # Change the code inside this function

assert(return_new_string_complex('banana', 'a', 2) == 'banna')
assert(return_new_string_complex('mississipi', 'i', 3) == 'mississpi')
assert(return_new_string_complex('aaddaddaa', 'a', 3) == 'aaddddaa')
assert(return_new_string_complex('paper', 'r', 1) == 'pape')
assert(return_new_string_complex('ghost', 's', 2) == 'ghost')

### Datetime
## 3. You need to build a tool to determine the number of vacation days needed to be granted. The function
## takes a start date and end date to the vacation and should return the number of vacation days needed.
## This function should take into account weekends and holidays.

def get_vacation_days(start_date: datetime.date, end_date: datetime.date):
    return None # Change the code inside this function
