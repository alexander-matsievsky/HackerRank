import sys


def window(iterable, n):
    window = []
    for x in iterable:
        if len(window) >= n:
            yield window
            window = []
        window.append(x)
    if len(window) > 0:
        yield window


[_, *lines] = list(sys.stdin)
students = [[name.strip(), float(grade)] for [name, grade] in window(lines, 2)]
second_lowest_grade = sorted(set(grade for [_, grade] in students), reverse=True)[-2]
print(sep='\n', *sorted(name for [name, grade] in students if grade == second_lowest_grade))
