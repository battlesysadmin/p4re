name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dictionary = {}
for line in handle:
    if line.startswith('From '):
        words = line.split()
        if words[1] not in dictionary:
            dictionary[words[1]]=1
        else:
            dictionary[words[1]] = dictionary[words[1]] + 1
largest = None
winner = None
for email, count in dictionary.items():
    if largest is None or count > largest:
        winner = email
        largest = count
print winner, largest
