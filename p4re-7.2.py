# Use program that prompts for a file name, then opens that file and reads 
# through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and 
# compute the average of those values and produce an output as shown below.
# You can download the sample data at http:
# //www.pythonlearn.com/code/mbox-short.txt when you are testing below enter #mbox-short.txt as the file name. the file name mbox-short.txt as the file name

'''
text = "X-DSPAM-Confidence:    0.8475";
index = text.find(':')
number = text[index+1:]
num = number.strip()
print float(num)
'''

fname = raw_input("Enter file name: ")
try:
    fh = open(fname)
    count = 0
    total = 0
except:
    fh = open('mbox-short.txt')
    count = 0
    total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1
    index = line.find(':') 
    sc = line[index+1:]
    score = sc.strip()
    total = total + float(score) 
print "Average spam confidence:",total / count

