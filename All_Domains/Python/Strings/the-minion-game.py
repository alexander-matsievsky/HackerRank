def sub_string_count(string, predicate):
    sub_string_count = 0
    string_len = len(string)
    for i in range(0, string_len):
        if predicate(string[i]):
            sub_string_count += string_len - i
    return sub_string_count


def is_vowel(letter):
    return letter in 'AEIOU'


def is_consonant(letter):
    return not is_vowel(letter)


string = input()
stuart = sub_string_count(string, is_consonant)
kevin = sub_string_count(string, is_vowel)
if stuart > kevin:
    print('Stuart {}'.format(stuart))
elif kevin > stuart:
    print('Kevin {}'.format(kevin))
else:
    print('Draw')
