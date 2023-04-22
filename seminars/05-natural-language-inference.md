## 2022-05-27 Natural language inference

S. R. Bowman, G. Angeli, C. Potts, and C. D. Manning. [A large annotated corpus for learning natural language inference.](https://www.aclweb.org/anthology/D15-1075/) In Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing (EMNLP). Association for Computational Linguistics, 2015.

* [video of the talk](https://vimeo.com/160168560)
* [the corpus](https://nlp.stanford.edu/projects/snli/)

A. Talman, A. Yli-Jyrä, and J. Tiedemann. [Sentence embeddings in NLI with iterative refinement encoders.](https://gu-se-primo.hosted.exlibrisgroup.com/permalink/f/15agpbr/TN_cambridgeS1351324919000202) Natural Language Engineering, 25(4):467–482, 2019.

* [slides](https://basement.ai/aarne/files/Seminar_Gothenburg_March_2019.pdf) from the CLASP seminar
* [slides](https://basement.ai/aarne/files/FoTran2018-Talman.pdf) from a workshop

[The FraCaS dataset](https://nlp.stanford.edu/\~wcmac/downloads/fracas.xml)

Collecting inference data. Only binary labels <https://www.dobnik.net/simon/semant-o-matic/create-conversation.en.mlt.php> and where labels are gradient <https://www.dobnik.net/simon/semant-o-matic/create-conversation.en.mlt2.php> Check them out to see what are the challenges for collecting data this way (and please answer non-randomly as the data will be added to the collected dataset). You can see the results of the first experiment in [this paper](https://aclanthology.org/W17-7203/).

### Questions to discuss

The first paper discusses a collection of corpus for natural language inference. The second paper provides a survey of approaches to NLI and presents a a solution where a neural language model is used to model inference. It also includes an evaluation of the model on different grammatical constructions.

Below are some points that you may want to consider when reading these papers:

For the first paper:

* Consider the notion of inference that is taken here when collecting the data for the dataset. How does this compare to the notion of the logical inference introduced in our first module and that is used in [the FraCaS dataset (Links to an external site.)](http://www-nlp.stanford.edu/\~wcmac/downloads/fracas.xml)?
* Why image scene descriptions are used; and why the images are not shown to the describers?
* The paper tests the collected dataset on existing NLI systems. From description and a discussion of results, what do you think are there strengths and weakness of each when modelling inference?

For the second paper:

* The NLI task involves training a neural network to predict one of the inference relations. Why is this task important for natural language processing / computational linguistics / language technology?
* In Figure 1 we see a general model architecture. What are the motivation behind different combinations of representations of sentence 1 and sentence 2, *u* and *v*?
* What is the reason for using a hierarchy of LSTM layers in the proposed model HBMP?
* In the second part of the paper the authors test the models on different datasets and linguistic constructions. What can we conclude (advantages and disadvantages) about the ability of neural networks to model natural language inference based on this analysis? What can we conclude about natural language inference itself?

### Points from the class

* Tests the theoretical strength of the representations but what is the actual practical use? Labels are not very useful for opractical tasks.
  * What applications?
  * Testing embeddings for different tasks. Tasks: sumarisation and question answering.
  * Building blocks for downstream tasks?
  * The way BERT is trained.
  * Tasks: sumarisation and question answering.
  * What does 70% accuracy on a particular label prediction tell us? Is that good for any task?
  * Do humans actually think like this?
  * A dog and a cat are playing hockey. Two animals are playing hockey. The system has to learn how general concepts are. How to bias the model to distinguish more general from more specific case.
* General representations
  * The way BERT is trained: the influence of context words on the semantics of a word, the relation between one sentence and another.
  * Training objective and the structure of the model will affect what kind of representations we learn.
  * If we can show that our representations can compare two sentences at the level of inference (specific training for this has not been incorporated in the training regime before) then we can be sure that we captured something useful about the basic semantic relation.
  * Inference is the basic linguistic operation that we want computer to master, a part of any task
  * Note that only DNNs models model inference as classification. 
    * Theorem provers infer by syntactically manipulating premises and conclusions.
    * Model builders try to build models from them.
    * Other classification-based approaches are turning them into features that are then classified: features range from syntactic (e.g. sentence length, etc) to lexical (presence of uni-grams and bi-grams), cf. the first model by Bowman et al.
    * With DNNs we assume that the semantic representations learned in un un/semi-supervised way will capture sufficient knowledge.
* What does 70% accuracy on a particular label prediction tell us? Is that good for any task?
  * Different performance on different labels: yes, no, neutral
  * Different performance on different examples of constructions: very useful to test on finer categories and not just in general, cf. SentenceEval, classification not of iference but of different linguistic phenomena, cf. Conneau et al.
* Do humans actually think like this? Inference in FraCas vs inference in the RTE task vs inference in the NLI dataset.
  * A dog and a cat are playing hockey. Two animals are playing hockey. The system has to learn how general concepts are. How to bias the model to distinguish more general from more specific cases. But what do we mean by general and specific?
  * But note: inference does not only involve lexical generality but also other syntactic and semantic linguistic constructions.
  * The difference between the examples in FraCaS (more general) and those in the NLI dataset (bound to event; what about inference that spans across events, e.g. temporal inference)
* What semantic representations are then useful for inference? Talman et al's model takes representations from different layers. We combine the sentence vectors by different compositional operations.
* Attention is all we need.
  * [A good explanation of attention](https://arxiv.org/abs/1612.01887) on the example of image captioning (we will return to this paper in the next course)

### Simon's points

On Bowman et al.

* Natural language inference: setence classification task, yes, no, don't know; entailment, contradiction
* NLI important for several tasks: question answering, semantic search, summarisation
* How DNNs learn representations of meaning? A good representation system should be able to deal with different linguistic features: corefernce, ambiguity, entailment, common sense knolwedhe, propositional attitued, modality, factivity and implicativity; i.e. categories from the FraCas
* A model must learn "compositional semantics" in an unsupervised way; we need good labelled data
* Datasets:
  * FraCaS, written by hand by experts, particular linguistic features; not quite open natural language
  * RTE datasets; natural language examples, create by users and validated by humans
  * SICK dataset; scene descriptions, human written and validated
  * DG: denotation graphs; short phrase pairs, hypothesis is some kind of a summary of a sentence; automatically labelled
  * Levy dataset: entialment graphs over relation triplets, formalised predicate and argument relations between premises and hypotheses; automatically labelled
  * PPDB Paraphrase dataset: short phrases automatically labelled for entailment
* SNLI Stanford Natural Language Corpus:
  * AMT, written and labelled by humans
  * co-reference issue: A boat sank in the Pacific vs A boat sank in the Atlantic: the same or different events? Contradition if we always assume that two sentences describe one event. But then contradiction also if we give completely different sentences. We need a category neutral, but then it is hard to find contradictions. We would need a general sentence like No boat has ever sunk in the Atalntic ocean.
  * Solution: use only a caption of the photo (and think of a photo) and your knowledge about the world write a sentence that is true given the caption (entailment), one sentence that might be true of a sentence (neutral), and one sentence that is definitely false given a photo. Situation is fixed by the imaginary photo.
  * Flickr30k photos and descriptions.
  * *Entailment:* P: Two women are embracing while holding to go packages. H: Two women are holding packages.
  * *Neutral:* P: A man in a blue shirt standing in front of a garage-like structure with geometric designs. H: A man repaiaring a garage.
  * *Contradiction:* P: A man selling donuts to a customer during a world exhibition held in the city of Angeles. H: A woman drinks her coffee in a small cafe.
  * Two sentences were written by different people. Disfavours syntact allignment.
  * Spelling and errors are rare.
  * Contradictions are often related to their premises. (Problem: the model could just meausre overlap to detect contradictions)
  * Validation: relabel 10% of the total data including everythjing for dev and test set. In addition to the original label, collect 4 more labels and take the majority vote; the winning label is the gold label; 58.3% unanimous vote; 32.9% 3+4 consensus including the author; 6.8% 3-4 vote not including the author, 2% no consensus for any label, these were labelled as unknown
* Evaluation
  * Simple logistic regression modells: (i) premise and hypothesis verlap: BLEU score, length difference, word overlap; (ii) lexicalised features: unigram, bigram, cross-unigram, cross-bigram between P and H
  * Neural network models: LSTMs for premission and hypothesis; feed them to three linear layesr with tanh and a softmax at the end
  * Best results from lexicalised classifier 78.2% while the DNNs 77.6%
  * Lexicalised models (including DNNs) improve when we collect more data
  * Compared the models from the Excitment Open Platform (Pado et al)
  * https://nlp.stanford.edu/projects/snli
* Limitations of the dataset: focuses on simgle events that are represented in the images; what about semamntic relations through time, e.g. videos?
* PPDP is on type level but SNLI is describing scenes; what is the overalap of scenes; boats sinking, etc.

On Talman et al.

* a hierarchy of bidirectional LSTM and max pooling layers that implements an iterative refinement strategy
* Two approaches: (i) separate representation of each sentence and then classification; (ii) cross-attention between sentences; Conneau et al 2017 explore different ways of encoding sentences;
* Treating the hypothesis and premise sentences together and focusing on the relationship between those sentences yields better results (Tay et al. 2018; Chen et al. 2017a). These methods are focused on the inference relations rather than the internal semantics of the sentences.
* Model on p.3 similar to Bowman (i.e. individual sentence representations) but sentences are combined by concatenated versions of u, v (u-v), (u\*v), different ways in which the sentence vectors can relate; the hidden layers of a bi-directional LSTM are max-pooled to prodcue these vectors; max-pooling is done after each bi-LSTM layer; different bi-LSTMs are stacked on the top of each other where each LSTM layer receives the hidden output of the previous layer as well as the original word embeddings: they call this iterative refinement which allows progressive learning of structure and lignuistic features, see p.4
* The model reaches 86.6% accuracy on the SNLI dataset
* MultiNLI (Williams et al. 2018) consists of sentence pairs from **10 distinct genres** of both written and spoken English. The dataset is divided into training (392,702 pairs), development (20,000 pairs), and test sets (20,000 pairs). Approximately 1000 sentence pairs annotated with linguistic properties of the sentences.
* SciTail: SciTail (Khot et al. 2018) is an NLI dataset created from multiple-choice science exams consisting of 27k sentence pairs. Each question and the correct answer choice have been converted into an assertive statement to form the hypothesis.
* Breaking NLI (Glockner, Shwartz, and Goldberg 2018) is a test set (8,193 pairs) which is constructed by taking premises from the SNLI training set and constructing several hypotheses from them by changing at most one word within the premise.
* SentEval: SentEval (Conneau et al. 2017; Conneau and Kiela 2018) is a library for evaluating the quality of sentence embeddings. It contains 17 downstream tasks as well as 10 probing tasks. The downstream datasets included in the tests were MR movie reviews, CR product reviews, SUBJ subjectivity status, MPQA opinion-polarity, SST binary sentiment analysis, TREC question-type classification, MRPC paraphrase detection, SICK-Relatedness (SICK-R) semantic textual similarity, SICK-Entailment (SICK-E) NLI, and STS14 semantic textual similarity. The probing tasks evaluate how well the sentence encodings are able to capture the following linguistic properties: length prediction, word content analysis, tree depth prediction, top constituents prediction, word order analysis, verb tense prediction, subject number prediction, object number prediction, semantic odd man out, and coordination inversion.
* A comparison how this model compares with other models on these datasets; it does not always win; shows that different models are good for different datasets/tasks
* Compared also with the InferSent (Conneau et al. 2017), p.9 how it performs on different labels of the NLI datasets: SNLI, MULTINLI and SciTail; neutral seems to be hard to predict but not on SciTail (here there is no contradiction label just entail)
* Evaluation of performance on sentences with particular linguistic features; the HBMP model outperforms InferSent with antonyms, coreference links, modality, negation, paraphrases, and tense differences. The performance on different linguistic features varies overall.
* Evaluation on the Breaking NLI (Glockner et al. 2018)
* How does the model compare on other tasks? Transfer learning and testing on the SentEval sentence embedding library which tests predicting different properties of sentences, p.13 SentLentgh, WC, TreeDepth, TopConst, BShift, Tense, SubjNum, ObjNum, SOMO, CordInv (Conneau et al. 2017).
* Datasets like SNLI and MultiNLI contain annotation artifacts which help neural network models in classification, allowing decisions only based on the hypothesis sentences as their input. (Gururangan, Swayamdipta, Levy, et al. (2018) and Poliak, Naradowsky, Haldar, et al. 2018)
* What kind of semantic information the different layers are able to capture and how they differ from each other?
* Do other architecture configurations could lead to even stronger results in NLI and other downstream tasks?
* Does the result carry over to multilingual setups and applications?

Other interesting papers

Conneau A. and Kiela D. (2018). SentEval: An evaluation toolkit for universal sentence representations. In Proceedings of the 11th Language Resources and Evaluation Conference. European Language Resource Association. Miyazaki, Japan: Phoenix Seagaia Conference Center, pp. 1699–1704.

Conneau A., Kiela D., Schwenk H., Barrault L. and Bordes A. (2017). Supervised learning of universal sentence representations from natural language inference data. In Proceedings of the 2017 Conference on Empirical Methods in Natural Language Processing. Association for Computational Linguistics. pp. 670–680.

Conneau A., Kruszewski G., Lample G., Barrault L. and Baroni M. (2018). What you can cram into a single vector: Probing sentence embeddings for linguistic properties. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers). Association for Computational Linguistics. pp. 2126–2136.

Glockner M., Shwartz V. and Goldberg Y. (2018). Breaking nli systems with sentences that require simple lexical inferences. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). Association for Computational Linguistics. pp. 650–655.

Williams A., Nangia N. and Bowman S.R. (2018). A broad-coverage challenge corpus for sentence understanding through inference. In Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers). Association for Computational Linguistics. pp. 1112–1122.

Khot T., Sabharwal A. and Clark P. (2018). Scitail: A textual entailment dataset from science question answering. In AAAI Conference on Artificial Intelligence.
