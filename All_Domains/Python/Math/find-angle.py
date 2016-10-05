import math

[AB, BC] = list(map(int, [input(), input()]))
radians = math.atan2(AB, BC)
print('%s°' % int(round(math.degrees(radians))))
