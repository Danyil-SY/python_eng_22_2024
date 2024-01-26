# Normalize phone

---

## Task and Solution

```py
'''
    Week #3. Task #3:
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
# Normalized phone numbers for SMS distribution:  ['+380671234567', '+380952345678', '+380441234567', 
# '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
```
