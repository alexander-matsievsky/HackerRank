import sys


def sub_strings_count(string, sub_string):
    sub_strings_count = 0
    string_length = len(string)
    sub_string_length = len(sub_string)
    for i in range(0, string_length):
        if i + sub_string_length > string_length:
            break
        all_matched = True
        for sub_i in range(0, sub_string_length):
            if not string[i + sub_i] == sub_string[sub_i]:
                all_matched = False
        if all_matched:
            sub_strings_count += 1
    return sub_strings_count


[string, sub_string] = list(sys.stdin)
print(sub_strings_count(string, sub_string))
