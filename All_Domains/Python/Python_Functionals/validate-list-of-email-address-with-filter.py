import re

N = int(input())
emails = (input().strip() for _ in range(0, N))
valid_email = re.compile(r'''
# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.
# The website name can only have letters and digits.
# The maximum length of the extension is 3.
^
[\w-]+ # username
@
[^\W_]+ # websitename
\.
.{,3} # extension
$
''', re.X)
print(sorted(filter(lambda email: valid_email.search(email), emails)))
