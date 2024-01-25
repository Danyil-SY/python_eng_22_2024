# Get days from today

---

## Task and solution

```py
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
```
