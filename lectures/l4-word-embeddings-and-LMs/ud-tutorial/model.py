import torch
import torch.nn as nn
from IPython import embed

class Tagger(nn.Module):
    def __init__(self, dimensions, n_words, n_tags):
        super(Tagger, self).__init__()
        self.embeddings = nn.Embedding(n_words, dimensions, padding_idx=0)
        self.rnn = nn.LSTM(dimensions, 
                           dimensions, 
                           bidirectional=True,
                           batch_first=True)
        self.dropout = nn.Dropout(0.3)
        
        self.predict = nn.Sequential(nn.Linear(dimensions*2, dimensions*2),
                                     nn.ReLU(),
                                     nn.Linear(dimensions*2, n_tags))

    def forward(self, words):

        raise embed()
    
        embedded_words = self.embeddings(words)
        sequential_representation, (h, c) = self.rnn(embedded_words)
        sequential_representation = self.dropout(sequential_representation)
        predictions = self.predict(sequential_representation)
        return predictions
