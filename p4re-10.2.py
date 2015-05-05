name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dictionary = {}

for line in handle:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        hour = time[0]
        if hour not in dictionary:
            dictionary[hour]=1
        else:
            dictionary[hour] = dictionary[hour] + 1
       
for hour in sorted(dictionary):
    print hour, dictionary[hour]

