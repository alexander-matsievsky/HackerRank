import sys
from collections import OrderedDict

[_, *items] = list(sys.stdin)
items = [(' '.join(item.split()[0:-1]), int(item.split()[-1])) for item in items]
purchases = OrderedDict()
for (item_name, price) in items:
    purchases[item_name] = purchases.get(item_name, 0) + price
print(sep='\n', *['{} {}'.format(item_name, net_price) for item_name, net_price in purchases.items()])
