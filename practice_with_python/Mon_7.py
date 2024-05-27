fname = input('Enter file: ')
handle = open(fname)

di = dict()
for line in handle:
    if line.startswith('From:'):
        line = line.rstrip().split()
        word = line[1]
        di[word] = di.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in di.items():
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count
print(bigword,bigcount)

