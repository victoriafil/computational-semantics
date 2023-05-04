from itertools import chain

with open('lorem.txt') as f:
    data = []
    for line in f.readlines():
        line = line.rstrip().lower()
        # tokenization
        # keep punctuation: line.replace(',', ' ,').split()
        line = [x.replace('.', '').replace(',', '') for x in line.split()]
        data.append(line)

x = list(chain.from_iterable(data))
vocabulary = set(x)
# for translating words to integers
word2i = dict([(x,i) for i, x in enumerate(vocabulary, start=1)])
# for translating integers to words
i2word = dict([(i,x) for x, i in word2i.items()])

# simple create a batch from the first two examples in the dataset
batch = data[:2]
max_len = max([len(x) for x in batch])

encoded_batch = [[word2i[w] for w in x]+[0]*(max_len-len(x)) for x in batch]