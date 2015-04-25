abc = None

lst = [1, 2, 3]

for val in lst:
   if abc == None or val > abc:
      abc = val


print abc
