import re
import sys
from email.utils import parseaddr, formataddr

addresses = [parseaddr(address.strip()) for address in sys.stdin][1:]
valid_email = re.compile(r'''
# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
# The username starts with an English alphabetical character, and any subsequent characters consist of one or more of
#   the following: alphanumeric characters, -,., and _.
# The domain and extension contain only English alphabetical characters.
# The extension is 1, 2, or 3 characters in length.
^
[^\W\d_][\w.-]+ # username
@
[^\W\d_]+ # domain
\.
[^\W\d_]{1,3} # extension
$
''', re.VERBOSE)
print(sep='\n', *[formataddr((name, email)) for name, email in addresses if valid_email.match(email)])
