from collections import defaultdict
from toolz import valmap
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as opt
from load_data import batcher, read_ud
from model import Tagger
from IPython import embed
from pprint import pprint
from sklearn.metrics import f1_score, precision_score, recall_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DEVICE = torch.device('cpu') # change this to torch.device('cuda:0') if you have a GPU

def train(model, optimizer, loss_f, batch_iterator):
    model.train()
    losses = []
    for j, batch in enumerate(batch_iterator):
        # sent the batch of words to the model
        y_hat = model(batch.words)

        # fix shape of output
        y_hat = y_hat.reshape(y_hat.size(0)*y_hat.size(1), y_hat.size(2))

        # calculate loss
        loss = loss_f(y_hat, batch.tags.flatten())

        # calculate gradients and optimize
        loss.backward()
        optimizer.step()

        # remove current gradients
        optimizer.zero_grad()
        
        losses.append(loss.item())
        if (j%100) == 0:
            print(np.mean(losses))

    return model, losses

def test(model, batch_iterator):
    model.eval()
    accuracy = []
    tags = []
    y_tags = []
    
    for j, batch in enumerate(batch_iterator):
        with torch.no_grad():
            # disable gradients and sent the batch of sentences to the model
            y_hat = model(batch.words)
        
        # flatten everything
        batch_tags = batch.tags.flatten()
        y_hat = y_hat.argmax(-1).flatten()
        
        # add the accuracy as 1's and 0's
        accuracy += [int(x==y) for x, y in zip(y_hat, batch_tags)]
        tags += batch_tags.tolist()
        y_tags += y_hat.tolist()
        
        #if j == 100:
        #    return model, accuracy, tags,  y_tags
        
    return model, accuracy, tags, y_tags

def remove_pad(tags, y_tags, accuracy):
    # remove padding
    paddles_predictions = list(filter(lambda x: x[0] != 0, zip(tags, y_tags, accuracy)))
    return list(zip(*paddles_predictions))

def per_tag_accuracy(accuracy, tags, tag2idx):
    # create a dictionary to store tag accuracy
    per_tag_acc = defaultdict(list)
    # reverse dictionary
    idx2tag = {v:k for k, v in tag2idx.items()}
    # translate tag indexes to part of speech tags
    tags = [idx2tag[x] for x in tags]
    # populate dictionary
    for tag, acc in zip(tags, accuracy):
        per_tag_acc[tag].append(acc)
    # calculate the accuracy for each tag
    return valmap(np.mean, per_tag_acc)

def confusion_matrix(tags, y_tags, num_tags):
    cm = np.zeros((num_tags, num_tags), dtype=int)
    # rows are the correct labels, and column what the model assigned
    for y, y_hat in zip(tags, y_tags):
        cm[y, y_hat] += 1    
    return cm

def main():
    n_epochs = 1
    # collect our dataset
    datasets, word2idx, tag2idx = read_ud() 

    # create model, optimizer and loss function
    model = Tagger(64, len(word2idx), len(tag2idx)).to(DEVICE)
    optimizer = opt.Adam(model.parameters(), lr=0.0001)
    loss_f = nn.CrossEntropyLoss(ignore_index=0)

    for epoch in range(n_epochs):
        # create an iterator that goes through the whole dataset
        batch_iterator = batcher(datasets['train'], word2idx, tag2idx)
        model, epoch_loss = train(model, optimizer, loss_f, batch_iterator)
        print(epoch, np.round(np.mean(epoch_loss), 4))

    # evaluate the model
    batch_iterator = batcher(datasets['test'], word2idx, tag2idx)
    model, accuracy, tags, y_tags = test(model, batch_iterator)
    
    # remove the predictions for padded tokens
    tags, y_tags, accuracy = remove_pad(tags, y_tags, accuracy)
    
    # For part of speech tagging
    num_tags = len(tag2idx)
    cm = confusion_matrix(tags, y_tags, num_tags)
    tags_for_pd = dict(sorted(tag2idx.items(), key=lambda x: x[1])).keys()
    cm = pd.DataFrame(cm, tags_for_pd, tags_for_pd)
    # take the sum of rows (axis 0) and divide it by the value in the column (axis 1)
    cm = cm.div(cm.sum(axis=0), axis=1)
    # percetage of TAG which are predicted to be TAG 
    sns.heatmap(cm, annot=True)
    ### uncomment the line below if you want to see the confusion matrix:
    #plt.show()
    plt.clf()
    
    # caluclate the accuracy for each tag
    tag_acc = per_tag_accuracy(accuracy, tags, tag2idx)
    
    print('----------------------------------------')
    pprint(tag_acc)
    print(np.mean(accuracy))
    
    raise embed()
    
    #print('f1:', f1_score(tags, y_tags, average='macro'))
    # # precision: the ratio between the correct predictions and the total predictions made
    #print('precision:', precision_score(tags, y_tags, average='macro', zero_division=0))
    # # recall: the ratio of the correct predictions and the total number of correct examples.
    #print('recall:', recall_score(tags, y_tags, average='macro'))

if __name__ == '__main__':
    main()