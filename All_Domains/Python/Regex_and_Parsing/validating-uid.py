import re


def is_valid_uid(uid):
    # It must contain at least 2 uppercase English alphabet characters.
    # It must contain at least 3 digits (0 - 9).
    # It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
    # No character should repeat.
    # There must be exactly 10 characters in a valid UID.
    return (
        re.match(r'^[a-zA-Z\d]{10}$', uid) and
        re.search(r'(?:[^A-Z]*[A-Z][^A-Z]*){2,}', uid) and
        re.search(r'(?:[^\d]*\d[^\d]*){3,}', uid) and
        not re.search(r'(.).*?\1', uid)
    )


print(sep='\n', *('Valid' if is_valid_uid(input().strip()) else 'Invalid' for _ in range(0, int(input()))))
