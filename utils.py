import re

def to_number(string):
    multipliers = {
        'K': 1000,
        'M': 1000000
    }

    letter_search = re.search(r'[A-Z]', string)
    if letter_search == None: return int(string)

    multiplier = letter_search.group()
    return int(float(string[:-1]) * multipliers[multiplier])
