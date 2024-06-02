import re

print("yes" if re.match("^([a-z]|_)*.py$", input().lower()) else "no")
