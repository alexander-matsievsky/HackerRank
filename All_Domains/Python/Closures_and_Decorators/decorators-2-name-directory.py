import sys


def serialize_people(f):
    def inner(people):
        return ['{} {} {}'.format('Ms.' if sex == 'F' else 'Mr.', first, last) for (first, last, _, sex) in f(people)]

    return inner


@serialize_people
def sort_people(people):
    return sorted(people, key=lambda person: person[2])


[_, *people] = list(sys.stdin)
people = [tuple(person.split()) for person in people]
print(sep='\n', *sort_people(people))
