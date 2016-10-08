from collections import namedtuple

[N, Student] = [int(input()), namedtuple('Student', input())]
students = [Student(*input().split()) for _ in range(0, N)]
print('{:.2f}'.format(sum(map(lambda student: float(student.MARKS), students)) / len(students)))
