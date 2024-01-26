# Get numbers ticket

---

## Task and Solution

```py
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
```
