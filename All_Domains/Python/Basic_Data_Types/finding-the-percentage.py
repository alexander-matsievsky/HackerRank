import sys

[_, *students, name] = list(sys.stdin)
students = [student.split(' ') for student in students]
students = [{
                'name': name.strip(),
                'math': float(math),
                'physics': float(physics),
                'chemistry': float(chemistry)
            } for [name, math, physics, chemistry] in students]
index = {}
for student in students:
    index[student['name']] = student

print("{:.2f}".format((index[name]['math'] + index[name]['physics'] + index[name]['chemistry']) / 3))
