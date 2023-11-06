text = 'Hi there you here exa_mple@example.com @blabla some more text here and there another@example.de'

import re

pattern = re.compile("[^ ]+@[^ ]+.[a-z]+")
matches = pattern.findall(text)
print(matches)
