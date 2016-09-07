import re
infile = input('Enter file directory: ')

with open(infile, "r") as f:
    read_data = f.read()

s = ' '.join(read_data.split()).split(' ')
wcount = len(' '.join(read_data.split()).split(' '))

counts = [];
words = [];

for w in s:
    if w not in words:
        counts.append(s.count(w))
        words.append(w)
uwords = len(counts)

s_r = re.sub(r'[A-Z][a-z]{0,1}\.', '', ' '.join(read_data.split()))
s_p = s_r.split('.')

lengths = [];
for i in s_p:
    lengths.append(len((' '.join(i.split()).split(' '))))
avg_p_len = sum(lengths)/len(lengths)

print("Total word count: "+ str(wcount))
print("Total unique words: "+ str(uwords))
print("Number of sentences: "+ str(len(s_p)))
print("Average sentence length: "+ str(round(avg_p_len,2))+" words")

f.closed
