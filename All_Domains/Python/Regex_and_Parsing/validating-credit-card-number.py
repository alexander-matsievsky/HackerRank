import re


def is_valid_credit_card(credit_card):
    # It must NOT have 4 or more consecutive repeated digits.
    return not re.search(r'(\d)(-?\1-?){3,}', credit_card) and re.match(r'''
    # It must start with a 4, 5 or 6.
    # It must contain exactly 16 digits.
    # It must only consist of digits (0-9).
    # It may have digits in groups of 4, separated by one hyphen "-".
    # It must NOT use any other separator like ' ' , '_', etc.
    ^
    [456]\d{3}(-?\d{4}){3}
    $
    ''', credit_card, re.X)


print(sep='\n', *('Valid' if is_valid_credit_card(input().strip()) else 'Invalid' for _ in range(0, int(input()))))
