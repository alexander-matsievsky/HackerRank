import re

postal_code = input().strip()
print(
    bool(re.match(r'^[^\D0]\d{5}$', postal_code)) and
    len(re.findall(r'(?=(.).\1)', postal_code)) <= 1
)
