import datetime

### String Manipulation
## 1. Remove the second character 'a' from any of the strings passed into the function and return the result.
## For example, 'banana' should be return as 'banna'

def return_new_string_simple(name: str):
    if name.count('a') > 1:
        return name[:name.index('a', name.index('a')+1)] + name[name.index('a', name.index('a')+1)+1:]
    else:
        return name

assert(return_new_string_simple('banana') == 'banna')
assert(return_new_string_simple('aaa') == 'aa')
assert(return_new_string_simple('pineapplepan') == 'pineapplepn')
assert(return_new_string_simple('mississauga') == 'mississaug')
assert(return_new_string_simple('paper') == 'paper')

# 2. Using the above written code, modify the code so the user can input the character they want to drop
# and the at which occurance
# E.g. Drop the 3rd 'i' in mississipi --> mississpi

def return_new_string_complex(name: str, char: str, occurance: int):
    if (len(name) - len(name.replace(char,"")) < occurance):
        return name
    else:
        temp_name = ""
        for n in range(0, occurance):
            pos = name.find(char)
            temp_name += name[:pos+1]
            name = name[pos+1:]
        
        return(temp_name[:len(temp_name) - 1] + name)
        
    # print(pos)
    # return name[0:pos] + name[pos+1:]
    # if name.count(char) >= occurance:
    #     indices = []
    #     for num, letter in enumerate(name):
    #         if letter == char:
    #             indices.append(num)
    #     return name[:indices[occurance-1]] + name[indices[occurance-1]+1:]
    # else:
    #     return name

# print(return_new_string_complex('banana', 'a', 2))

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
    from datetime import timedelta
    import holidays

    can_holidays = holidays.CAN
    num_of_busi_days = int((end_date-start_date).days)+1
    years = [year for year in range(int(start_date.year), int(end_date.year)+1)]
 
    for n in range(num_of_busi_days):
        day = start_date + timedelta(n)
        if day.isoweekday() > 5:
           print(day.date())
           num_of_busi_days -= 1
        elif day.date() in can_holidays(years = years).keys():
            print(day.date())
            num_of_busi_days -= 1
    return num_of_busi_days