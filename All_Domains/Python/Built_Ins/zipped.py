import sys

[_, *subjects] = list(sys.stdin)
subjects = [list(map(float, subject.split())) for subject in subjects]
print(sep='\n', *[sum(scores) / len(scores) for scores in zip(*subjects)])
