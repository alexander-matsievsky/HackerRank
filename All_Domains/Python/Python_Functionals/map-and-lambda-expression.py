N = int(input())
fibonacci = [0, 1]
for i in range(2, N):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print(list(map(lambda x: x ** 3, fibonacci[:N])))
