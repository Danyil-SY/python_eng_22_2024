# Get upcoming birthdays

---

## Task and Solution

```py
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
```
