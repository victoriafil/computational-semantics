
# coding: utf-8

# # Parsing language to SQL queries: NLTK 10.1

# ## We have a grammar

# In[1]:

from nltk.data import show_cfg
#show_cfg('grammars/book_grammars/sql0.fcfg')
show_cfg('file:sql0.fcfg')


# The FCFG grammar uses feature structures with rules represented in []; there is a SEM feature which represents the semantics of the string; semantics is an SQL representation; 'which' corresponds to 'SELECT'; 'in' and 'are' don't contribute anything; the terminal expressions are combined with other rules; ? indicates a variable (an addition to Python); + concatenates strings;
# 

# ## From strings to semantic representations

# In[2]:

from nltk import load_parser
#cp = load_parser('grammars/book_grammars/sql0.fcfg') # data from (Warren and Prereira, 1982)
cp = load_parser('file:sql0.fcfg')
query = 'What cities are located in China'
trees = list(cp.parse(query.split()))
answer = trees[0].label()['SEM']
answer = [s for s in answer if s] # makes a tuple a list
q = ' '.join(answer)
print(q)


# ## Evaluating a semantic representation in a model

# In[3]:

from nltk.sem import chat80
rows = chat80.sql_query('corpora/city_database/city.db', q)
# rows = chat80.sql_query('./city.db', q)
for r in rows: print(r[0], end=" ") # each row is a tuple from which we extract city

