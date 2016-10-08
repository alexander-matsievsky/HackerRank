import sys
from collections import Counter

[_, shoe_sizes, _, *customers] = list(sys.stdin)
shoe_sizes = list(map(int, shoe_sizes.strip().split(' ')))
customers = [tuple(map(int, customer.strip().split(' '))) for customer in customers]
inventory = Counter(shoe_sizes)
print(sum(price for (shoe_size, price) in customers
          if (inventory.subtract([shoe_size]), inventory[shoe_size] >= 0)[1]))
