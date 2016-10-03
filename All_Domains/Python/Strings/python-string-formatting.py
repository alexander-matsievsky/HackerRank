import sys

N = int(sys.stdin.read())
fmt = '{n:>Wd} {n:>Wo} {n:>WX} {n:>Wb}'.replace('W', str(len('{:b}'.format(N))))
print('\n'.join(fmt.format(n=n) for n in range(1, N + 1)))
