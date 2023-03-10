import re

myStr = "peter pipper picked a peck of pickled pepper"
print(re.findall(r'(\w+)', myStr, flags=re.IGNORECASE))