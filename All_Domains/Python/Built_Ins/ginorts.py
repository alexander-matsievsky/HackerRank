def sort_order(s):
    if s.islower():
        return s.upper()
    elif s.isupper():
        return s.lower()
    elif int(s) % 2 == 1:
        return 'z0' + s
    return 'z1' + s


print(sep='', *sorted(input(), key=sort_order))
