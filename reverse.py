
with open('a.txt', 'r') as f:
 
  lines = f.readlines()


with open('b.txt', 'w') as f:
  
  for line in reversed(lines):
   
    f.write(line[::-1])
