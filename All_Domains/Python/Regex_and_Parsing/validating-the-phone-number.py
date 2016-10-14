import re
import sys

mobile_numbers = [mobile_number.strip() for mobile_number in sys.stdin][1:]
print(sep='\n', *['YES' if re.match(r'^[789]\d{9}$', mobile_number) else 'NO' for mobile_number in mobile_numbers])
