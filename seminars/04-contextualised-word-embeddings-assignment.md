# S4: Contextualised word embeddings

This assignment is a part of the preparation for the seminar on 12 May.

Please have a look [here](https://canvas.gu.se/courses/51974/pages/seminar-assignments-and-discussions) for how to prepare for the seminar.

In this seminar we will look at contextualised word embeddings. Previously we have learned word embeddings and language models as separate representations but which can be trained in the same end-to-end task. In this seminar we will look at the recent developments where both tasks have been integrated more closely.

When predicting a sequence of words, a mechanism of self-attention has been introduced which weights the importance of the previous generated words for the prediction of the next word. Organising attention heads over several layers allows us to learn structural dependencies between words at different levels of abstraction.

The development lead to pre-training very large language models that capture very fine grained semantic and world common-sense knowledge. These can be then used in particular NLP tasks whose performance has been greatly improved. However, training and using these large-scale models comes at cost. Firstly, training requires large (and expensive) computing infrastructure (not available to everyone) which consumes a lot of energy. Secondly, the models are trained on texts found on the web, but such texts do not represent all social groups equally and therefore the models capture particular social biases.

* J. Devlin, M. Chang, K. Lee, and K. Toutanova. [BERT: pre-training of deep bidirectional transformers for language understanding.](http://arxiv.org/abs/1810.04805) arXiv, arXiv:1810.04805 [cs.CL]:1–14, 2018.
* E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell. [On the dangers of stochastic parrots: Can language models be too big?](https://doi.org/10.1145/3442188.3445922) In Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, FAccT ’21, pages 610–623, New York, NY, USA, 2021. Association for Computing Machinery.

Optional further reading (quite advanced):

* A.Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A.N. Gomez, L􏰀. Kaiser, and I. Polosukhin. [Attention is all you need.](https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf) In Advances in Neural Information Processing Systems, pages 5998–6008, 2017.
* M. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee, and L. Zettlemoyer. [Deep contextualized word representations.](https://www.aclweb.org/anthology/N18-1202) In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers), pages 2227–2237, New Orleans, Louisiana, June 2018. Association for Computational Linguistics.
* A. Radford, K. Narasimhan, T. Salimans, and I. Sutskever. [Improving language understanding by generative pre-training.](https://openai.com/blog/language-unsupervised/) Technical report, OpenAI, 2018.

Below are some points that you may want to consider when reading these papers.

For the first paper:

* How does BERT compare with word embeddings and a recursive language model?
* Word tokenisation?
* What layers and representations should we use?

For the second paper:

* Do you agree with the authors of the paper?
* How can we do better NLP?

The assignment is marked with complete/incomplete with a further feedback on a 7 level scale where 4 is sufficient to complete the assignment; 5 is good solid work; 6 is excellent work that covers most of the assignment; and 7 is creative work that goes beyond the assignment.