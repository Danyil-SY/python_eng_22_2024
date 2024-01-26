'''
    Week #3. Task #1:
    Create a function get_days_from_today(date) that calculates 
    the number of days between a specified date and the current date.
'''

from datetime import datetime


# Calculate the number of days between a given date and the current date
def get_days_from_today(date):
    try:
        converted_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return 'Incorrect date format!'

    date_now = datetime.today() 

    difference_in_days = (converted_date - date_now).days

    return difference_in_days

# Test data
test_data = [
    # Correct Formats
    '2024-05-23',
    '2024-12-01',
    '2023-01-15',
    '2023-11-30',

    # Wrong Formats
    '2023-05-35',   # Incorrect day
    '2022-13-01',   # Incorrect month
    '2023/05/23',   # Wrong separator
    '23-05-2023'    # Wrong order
]

# Check
for date in test_data:
    result = get_days_from_today(date)
    print(f'{date}: {result}')

# The result:
#
# 2024-05-23: 118
# 2024-12-01: 310
# 2023-01-15: -376
# 2023-11-30: -57
# 2023-05-35: Incorrect date format!
# 2022-13-01: Incorrect date format!
# 2023/05/23: Incorrect date format!
# 23-05-2023: Incorrect date format!


####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################


'''
    Week #3. Task #2:
    To win the main prize in a lottery, it is necessary to match 
    several numbers on the lottery ticket with randomly drawn 
    numbers within a specific range during the next draw. For example, 
    you may need to guess six numbers from 1 to 49 or five numbers 
    from 1 to 36, and so on.

    You need to write a function get_numbers_ticket(min, max, 
    quantity) that will help generate a set of unique random numbers 
    for such lotteries.

    The function should return a random set of numbers within the 
    specified parameters, with all the random numbers in the set 
    being unique.
'''

import random


# Generate a lsit of unique random numbers within a specified range
def get_numbers_ticket(min, max, quantity):
    if quantity > (max - min + 1):
        return 'Quantity of numbers exceeds the range available.'
    
    tickets = set()

    while len(tickets) < quantity:
        tickets.add(random.randint(min ,max))

    return sorted(list(tickets))
    
 # Test data
test_data = [
    # Correct data
    (1, 49, 6),
    (3, 42, 9),
    (43, 97, 3),
    (30, 50, 4),    

    # Wrong data
    (1, 49, 50),
    (3, 42, 43),
    (43, 49, 10),
    (30, 39, 15),    
]

# Check
for num_list in test_data:
    result = get_numbers_ticket(num_list[0], num_list[1], num_list[2])
    print(f'{num_list}: {result}')

# The result:
#
# (1, 49, 6): [14, 17, 22, 26, 40, 46]
# (3, 42, 9): [14, 22, 24, 28, 35, 36, 37, 40, 42]
# (43, 97, 3): [67, 76, 84]
# (30, 50, 4): [30, 34, 45, 48]
# (1, 49, 50): Quantity of numbers exceeds the range available.
# (3, 42, 43): Quantity of numbers exceeds the range available.
# (43, 49, 10): Quantity of numbers exceeds the range available.
# (30, 39, 15): Quantity of numbers exceeds the range available.


####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################


'''
    Week #3. Task #4:
    In your company, an active marketing campaign is being conducted through SMS 
    distributions. To do this, you collect customer phone numbers from the database, 
    but often encounter the issue that the numbers are recorded in various formats. 
    For example:

        "    +38(050)123-32-34"
        "     0503451234"
        "(050)8889900"
        "38050-111-22-22"
        "38050 111 22 11   "
        
    Your messaging service can effectively send messages only when phone numbers 
    are in the correct format. Therefore, you need a function that automatically 
    normalizes phone numbers to the required format, removing all unnecessary 
    characters and adding the country's international code if necessary.

    Develop a function normalize_phone(phone_number) that normalizes phone numbers 
    to a standard format, keeping only digits and the '+' symbol at the beginning. 
    The function takes one argument - a string with the phone number in any format 
    and transforms it into the standard format, keeping only digits and the '+' symbol. 
    If the number does not contain an international code, the function automatically 
    adds the '+38' code (for Ukraine). This ensures that all numbers will be suitable 
    for sending SMS.
'''

import re


# Find the normalized version of the phone number
def normalize_phone(phone_number):
    number = ''.join(re.findall('\+?\d', phone_number))

    number_length = len(number)

    if number_length == 10:
        return '+38' + number
    elif number_length == 11:
        return '+' + number
    elif number_length == 12:
        return '+' + number
    elif number_length == 13:
        return number
    else:
        return 'Invalid phone number format.'

# Test data
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

#Check
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS distribution: ", sanitized_numbers)

# The result:
#
# Normalized phone numbers for SMS distribution:  ['+380671234567', '+380952345678',  
# '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', 
# '+380501112222', '+380501112211']


####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################


'''
    Week #3. Task #4:
    Within your organization, you are responsible for organizing 
    birthday greetings for colleagues. To streamline this process, 
    you need to create a function called get_upcoming_birthdays 
    that will help you determine which colleagues need to be greeted.

    You have at your disposal a list called users, where each element 
    contains information about the user's name and their birthday. Since 
    colleagues' birthdays may fall on weekends, your function should also 
    take this into account and shift the greeting date to the next working 
    day if necessary.
'''

from datetime import datetime, timedelta


# Calculates upcoming birthdays within the next week for each user and 
# return a list of dictionaries, each containing the user's name and the 
# date for congratulations
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday_this_year

        days_until_birthday = (birthday - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday.weekday() >= 5:
                days_until_birthday += (7 - birthday.weekday())
                birthday += timedelta(days_until_birthday)

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

# Test data
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice", "birthday": "2024.01.28"},
    {"name": "Bob", "birthday": "2023.12.01"},
    {"name": "Charlie", "birthday": "2024.05.23"},    
]

# Check
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

# The result:
#
# Список привітань на цьому тижні: [{'name': 'Jane Smith', 'congratulation_date': '2024.01.30'}, 
# {'name': 'Alice', 'congratulation_date': '2024.01.31'}]
