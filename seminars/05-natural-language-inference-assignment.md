# S5: Natural language inference

This assignment is a part of the preparation for the seminar on 27 May.

Please have a look [here](https://canvas.gu.se/courses/51974/pages/seminar-assignments-and-discussions) for how to prepare for the seminar.

In this seminar we return the question of natural language inference (NLI): what do mean by natural language inference, how it is modelled in distributional representations using neural networks and how does the notion of inference captured in these models relate to the notion of inference we model with logic-based approaches, theorem provers and models builders.

In this seminar we will look at the following two papers:

* S. R. Bowman, G. Angeli, C. Potts, and C. D. Manning. [A large annotated corpus for learning natural language inference.](https://www.aclweb.org/anthology/D15-1075/) In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP). Association for Computational Linguistics, 2015.
  * A. Talman, A. Yli-Jyrä, and J. Tiedemann. [Sentence embeddings in NLI with iterative refinement encoders.](https://gu-se-primo.hosted.exlibrisgroup.com/permalink/f/15agpbr/TN_cambridgeS1351324919000202) Natural Language Engineering, 25(4):467–482, 2019.
  * Optional additional reading and helpful background:
    * **Tutorial with video:** S. Bowman and X. Zhu. [Deep learning for natural language inference.](https://www.aclweb.org/anthology/N19-5002) In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Tutorials, pages 6–8, Minneapolis, Minnesota, June 2019. Association for Computational Linguistics.
    * A. Conneau, D. Kiela, H. Schwenk, L. Barrault, and A. Bordes. [Supervised learning of universal sentence representations from natural language inference data.](http://arxiv.org/abs/1705.02364) arXiv, arXiv:1705.02364 [cs.CL]:1–12, 2017.
    * S. Hewitt. [Textual entailment with TensorFlow: Using neural networks to explore natural language.](https://www.oreilly.com/content/textual-entailment-with-tensorflow/) Tutorial and code, O’Reilly and TensorFlow, July 2017.
    * R. Cooper, D. Crouch, J. Van Eijck, C. Fox, J. Van Genabith, J. Jaspars, H. Kamp, D. Milward, M. Pinkal, M. Poesio, et al. Using the framework. Technical report, Technical Report LRE 62-051 D-16, The FraCaS Consortium, 1996. <ftp://ftp.cogsci.ed.ac.uk/pub/FRACAS/del16.ps.gz>
    * Y. Bizzoni and S. Dobnik. [Distributional semantic models for detection of textual entailment.](https://gup.ub.gu.se/publication/249970) In J. Björklund and S. Stymne, editors, Proceedings of the Sixth Swedish language technology conference (SLTC), pages 1–5, Umeå, 17–18 November 2016. Umeå University.
    * S. Chatzikyriakidis, R. Cooper, S. Dobnik, and S. Larsson. [An overview of natural language inference data collection: The way forward?](https://gup.ub.gu.se/publication/257683?lang=en) In C. Gardent and C. Retoré, editors, Proceedings of IWCS 2017: 12th International Conference on Computational Semantics, Workshop on Computing Natural Language Inference, pages 1–6, Montpellier, France, 19–22 September 2017. Association for Computational Linguistics.

The first paper discusses a collection of corpus for natural language inference. The second paper provides a survey of approaches to NLI and presents a a solution where a neural language model is used to model inference. It also includes an evaluation of the model on different grammatical constructions.

Below are some points that you may want to consider when reading these papers:

For the first paper:

* Consider the notion of inference that is taken here when collecting the data for the dataset. How does this compare to the notion of the logical inference introduced in our first module and that is used in [the FraCaS dataset](http://www-nlp.stanford.edu/~wcmac/downloads/fracas.xml)?
* Why image scene descriptions are used; and why the images are not shown to the describers?
* The paper tests the collected dataset on existing NLI systems. From description and a discussion of results, what do you think are there strengths and weakness of each when modelling inference?

For the second paper:

* The NLI task involves training a neural network to predict one of the inference relations. Why is this task important for natural language processing / computational linguistics / language technology?
* In Figure 1 we see a general model architecture. What are the motivation behind different combinations of representations of sentence 1 and sentence 2, *u* and *v*?
* What is the reason for using a hierarchy of LSTM layers in the proposed model HBMP?
* In the second part of the paper the authors test the models on different datasets and linguistic constructions. What can we conclude (advantages and disadvantages) about the ability of neural networks to model natural language inference based on this analysis? What can we conclude about natural language inference itself?

The assignment is marked with complete/incomplete with a further feedback on a 7 level scale where 4 is sufficient to complete the assignment; 5 is good solid work; 6 is excellent work that covers most of the assignment; and 7 is creative work that goes beyond the assignment.