from datetime import datetime

fmt = '%a %d %b %Y %H:%M:%S %z'
T = int(input())
for _ in range(0, T):
    t1 = datetime.strptime(input().strip(), fmt)
    t2 = datetime.strptime(input().strip(), fmt)
    print(abs(int((t2 - t1).total_seconds())))
