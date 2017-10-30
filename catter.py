from collections import defaultdict
from getch import getch

f = open('sorted_tokens.txt')
cat_to_things = defaultdict(set)
for line in f:
  token = line.strip()
  print token + ' ',
  c1 = getch()
  print c1,
  #cat = raw_input("{} ".format(token))
  if c1 == 'Q' or c1 == '\x03':
    break
  c2 = getch()
  print c2
  cat = c1+c2
  cat_to_things[cat].add(token)

with open('categorized.py', 'w') as f:
  s = repr(dict(cat_to_things))
  f.write(s+'\n')
