import sys


def standardize_phone_numbers(f):
    def inner(phone_numbers):
        return f(['+91 {} {}'.format(phone_number[-10:-5], phone_number[-5:]) for phone_number in phone_numbers])

    return inner


@standardize_phone_numbers
def sort_phone_numbers(phone_numbers):
    return sorted(phone_numbers)


[_, *phone_numbers] = list(sys.stdin)
phone_numbers = [phone_number.strip() for phone_number in phone_numbers]
print(sep='\n', *sort_phone_numbers(phone_numbers))
