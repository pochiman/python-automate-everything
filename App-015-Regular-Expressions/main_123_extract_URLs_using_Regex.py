with open('urls.txt', 'r') as file:
    content = file.read()

print(content)


import re

pattern = re.compile("https?://(?:www.)?[^ \n]+\.com")
matches = pattern.findall(content)
print(matches)
