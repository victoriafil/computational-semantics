from itertools import chain
from toolz import take
from IPython import embed
from collections import Counter, namedtuple
import random
import torch
import os

DEVICE = torch.device('cpu') # change this to torch.device('cuda:0') if you have a GPU

def read_ud():
    # just a complicated procedure to read universal dependencies
    vocabulary = []
    tags = set([])
    sentences = {'train':[], 'test':[], 'dev':[]}
    sentence = False
    for file in os.listdir('ud_data/'):
        with open(f'ud_data/{file}') as f:
            dataset = file.split('-')[-1].split('.')[0]
            for line in f.readlines():
                if line.startswith('# text = '):
                    if sentence and len(sentence[0]) > 3:
                        sentences[dataset].append(sentence)
                    # words, pos tags
                    sentence = [[],[]]
                    continue
                elif line.startswith('#') or line.split() == []:
                    continue
                else:
                    #print(line)
                    id, word, _, tag, _, _, _, dep_rel, *_ = line.rstrip().split('\t')
                    if '-' in id:
                        continue
                    vocabulary.append(word.lower())
                    tags.add(tag)
                    sentence[0].append(word.lower())
                    sentence[1].append(tag)
    
    # add a mapping from tags and words to indexes
    tag2idx = {x:i+1 for i, x in enumerate(tags)}
    tag2idx['PAD'] = 0
    vocabulary = create_word2idx(Counter(vocabulary))
    
    return sentences, vocabulary, tag2idx

def create_word2idx(vocabulary, min_freq=10):
    # remove words that does not occur very often!
    vocabulary = dict(filter(lambda x: x[1] >= min_freq, vocabulary.items()))
    vocabulary = list(vocabulary.keys())
    # add a token for padding, and a "catch all" token for the removed words
    vocabulary = ['PAD', 'UNK'] + vocabulary
    # map words to indexes
    return {x:i for i, x in enumerate(vocabulary)}

def x2idx(seq, to_idx):
    # all tags exist, but not all words!
    # for the words that don't exist in word2idx select the UNK token
    return list(map(lambda x: [to_idx.get(e, 1) for e in x], seq))

def create_batch(words, tags):
    Batch = namedtuple('Batch', ['words', 'tags'])

    max_seq_words = max([len(x) for x in words])
    max_seq_tags = max([len(x) for x in tags])

    # pad! (and we made sure earlier that the pad tokens have index 0)
    words = [x + [0]*(max_seq_words-len(x)) for x in words]
    tags = [x + [0]*(max_seq_tags-len(x)) for x in tags]

    return Batch(torch.LongTensor(words).to(DEVICE), torch.LongTensor(tags).to(DEVICE))

def batcher(dataset, word2idx, tag2idx, batch_size=8):
    random.shuffle(dataset)
    dlen = len(dataset)
    dataset = iter(dataset)

    for _ in range(int(dlen/batch_size)+1):
        batch = list(take(batch_size, dataset))
        if batch:
            words, pos = list(zip(*batch))
        else:
            StopIteration
        
        # translate words and tags to indexes
        words_as_idx = x2idx(words, word2idx)
        pos_as_idx = x2idx(pos, tag2idx)
        
        # create the batch
        batch = create_batch(words_as_idx, pos_as_idx)
        yield batch

if __name__ == '__main__':
    dataset, word2idx, tag2idx = read_ud()
    for x in batcher(dataset['train'], word2idx, tag2idx):
        raise embed()