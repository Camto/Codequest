import re

for _ in range(int(input())):
  print('(%s) %s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', int((input())'))) #Parenthesis
  print('%s-%s-%s' % tuple(re.findall(r'\d{4}$|\d{3}', '0123456789')) #Dashes
  print('%s.%s.%s' % tuple(re.findall(r'\d{4}$|\d{3}', '0123456789'))
#Periods