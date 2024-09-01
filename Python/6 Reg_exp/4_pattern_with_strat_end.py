import re

# Matches from beginning of line.
name = 'sriram'
mo = re.match('^sri', name)
print(mo.group())


# Matches from end of line.
name1 = 'sriram123'
m1 = re.match('rm123$', name1)
print(m1.group())


