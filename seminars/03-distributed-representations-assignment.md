# S3: Distributed representations

This assignment is a part of the preparation for the seminar on 27 April.

Please have a look [here](https://canvas.gu.se/courses/64394/pages/seminar-assignments-and-discussions) for how to prepare for the seminar.

In this seminar we will look at how we can learn distributed meaning representations and language models using neural networks. Similarly to the previous seminar we will discuss what semantic knowledge these representations capture and how do they relate to the notion of compositionality.

* Y. Bengio, R. Ducharme, P. Vincent, and C. Janvin. [A neural probabilistic language model.](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf) Journal of Machine Learning Research, 3(6):1137–1155, 2003. (Sections 3 and 4 are less relevant today and hence you can glance through them quickly. Instead, look at the Mikolov papers where they describe training word embeddings with the current neural network architectures.)
* M. Ghanimifard and S. Dobnik. [Learning to compose spatial relations with grounded neural language models.](https://gup.ub.gu.se/publication/257763?lang=en)[ ](https://canvas.gu.se/courses/22914/files/2936161/download?download_frd=1) In C. Gardent and C. Retoré, editors, Proceedings of IWCS 2017: 12th International Conference on Computational Semantics, pages 1–12, Montpellier, France, September 19–22 2017. Association for Computational Linguistics.

Optional but helpful background and further reading:

* T. Mikolov, K. Chen, G. Corrado, and J. Dean. [Efficient estimation of word representations in vector space.](https://arxiv.org/pdf/1301.3781.pdf) arXiv preprint arXiv:1301.3781, 2013.
* T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean. [Distributed representations of words and phrases and their compositionality.](https://proceedings.neurips.cc/paper/2013/file/9aa42b31882ec039965f3c4923ce901b-Paper.pdf) In Advances in neural information processing systems, pages 3111–3119, 2013.
* M. Kågebäck and H. Salomonsson. [Word sense disambiguation using a bidirectional LSTM.](https://arxiv.org/pdf/1606.03568.pdf) In 5th Workshop on Cognitive Aspects of the Lexicon (CogALex). Association for Computational Linguistics, 2016.
* C. Manning. [Representations for language: From word embeddings to sentence meanings.](https://simons.berkeley.edu/talks/christopher-manning-2017-3-27) talk, Stanford University, Simons Institute, Berkeley, March 27th 2017. [slides](https://simons.berkeley.edu/sites/default/files/docs/6449/christophermanning.pdf)

Below are some points that you may want to consider when reading these papers.

For the first paper:

* Some concepts: syntagmatic and paradigmatic relations, one-hot vector representation, dense embeddings, word2vec, CBOW, skip-gram, Gensim, GloVe, LSTM
* What is the difference between distributional word vectors/matrices, word vectors with dimensionality reduction and word embeddings?
* What are the benefits and weaknesses of using word embeddings compared to other word representations mentioned in the previous point both in terms of the nature of representation and computational cost building and using them?
* What kind of word embeddings can we build; what are differences between?
* What is a probabilistic language model? How do word embeddings relate to a probabilistic language model?

For the second paper:

* Can compositionality be learned from data?
* Why do we ground our language model in perceptual informations/locations?
* To what degree are distributional composed representations interpretable?
* Are the representations that we have learned the same as those as we would expect from compositional rules?
* Neural networks are also compositional models in the sense that they are composed of units and each of these units defines some representations. Do you agree?
* To what degree can we say that a neural network has learned compositional functions like those in formal semantics?

The assignment is marked with complete/incomplete with a further feedback on a 7 level scale where 4 is sufficient to complete the assignment; 5 is good solid work; 6 is excellent work, covers most of the assignment; and 7: creative work that goes beyond the assignment.

<https://canvas.gu.se/courses/64394/assignments/210878>