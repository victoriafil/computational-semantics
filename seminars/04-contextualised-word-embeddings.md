## 2021-05-12 Contextualised word embeddings

J. Devlin, M. Chang, K. Lee, and K. Toutanova. [BERT: pre-training of deep bidirectional transformers for language understanding.](http://arxiv.org/abs/1810.04805) arXiv, arXiv:1810.04805 [cs.CL]:1–14, 2018.

### Questions to discuss

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

### Points from the class

* training large models
  * pre-training and masking, the role of the mask token
  * transformer architectures
  * quires, keys and values
* morphology and tokenisation: problem with morphologically rich languages, creating tokenisers for these languages?
* ethical and moral dilemmas
  * focus on English only, other languages?
  * problem with tokenisation: annotated datasets that are tokenised; BERT introduces its own WordPiece tokenisation; have to align the tokens/annotations from the dataset to WordPiece tokens
* Attention is all we need?
  * Context into account: perhaps even seeing into the future: solves the problem of semantic disambiguation
  * Learns structure; from local to more abstract dependencies; 
  * Language and structure and how we learn: Josh Tennenbaum
* How to improve language technology?
  * pre-training takes a lot of energy but then re-use saves it? Trust one company?
  * Environment is destroyed in communities that benefit the least of LT?
  * How we use the tool is what matters
  * Setting realistic goals: knowing where to stop; but we do want universally good models; where is the limit?
  * Ethical issues are speaking against single large models and therefore invalidate the environamental argument
  * Language models used for commercial purposes, aimed also to imrpove those domains; the net is not representative of human activity
  * How data is curated; what are good and bad words to remove form the dataset? A language technologist has to be an ethical judge? Shall we take this responsibility?
  * On one hand we want to cover all domains but on the hand wer do not want our systems to become abusive.
  * Internet users are not representative; different language use under anonymity
  * Google Books: language change question? Modern contemporary language?
  * Ranting without solutions? Repetatative. Solutions?
  * Pre-training and then application to a different domain: Kathrein's thesis defence: large language models are not necessarily useful when the domain changes slightly
  * Do language models understand language?

### Simon's points

On the Devlin's et al model.

* BERT: Bidirectional Encoder Representations from Transformers
* Features:
  * bi-directional, left and right
  * ELMo, Peters at el. 2018, uni-directional --> and <--- LSTMs
  * train it on a large corpus of text and save it; fine-tune some of its layers and the final task-specific layer
  * pre-trained reduces the amount of training and resources
  * tested on 11 NLP tasks, the GLUE benchmark
  * tasks: natural language inference, paraphrasing, NER, question answering
  * embeddings: word-embeddings, sentence embeddings, paragraph embeddings, document embeddings?
* Two approaches to **transfer learning**
  * a general task and a down-stream task
  * since we already learned the language, for a downstream task a fewer parameters need to be learned
  * feature-based: use a pre-trained model to encode text to features (ELMo, Peters et al., 2018)
  * freeze the weights of some / all previously trained and add an additional layer and only train (fine-tune) that
* Pre-trained uni-directional models are not suitable for fine-tuning on all tasks (e.g. those that require processing the entire sentence) BUT also bi-directional models are also not, e.g. the problem with generation
* Generalised model of transformers was introduced in Vaswani et al. (2017), see a tutorial here <http://nlp.seas.harvard.edu/2018/04/03/attention.html>
* `BERT_BASE:`L=12, H=768, A=12, Total Parameters=110M
* `BERT_LARGE:` L=24, H=1024, A=16, Total Parameters=340M
* Input: sum token, segment and position embeddings
  * token: WordPiece embeddings
  * segment: sentence 1, sentence 2
  * position embeddings: information about the order of the word in a sentence; somehow trained
  * `[CLS]` as the first token: classification embedding
  * `[SEP]`separates sentences
* learn general language representations with two objectives:
  * the masked language model (MLM), the Cloze task, predict the word that is replaced by MASK at a random position; softmax to get probabilities
  * problem: [MASK] is not going to be a token in the fine-tuning, need to bias learning towards the actual words rather than MASK: 15% of words of WordPiece tokens are chosen at random and then (i) in 80% of cases these replaced by MASK, (ii) in 10% of cases these are replaced by a random word, and (iii) in 10% of cases the word is unchanged; a transformer has to learn all of these distributions, MASK is introduced in 10% of 15% or 1.5% of tokens, does not hurt performance; the down-side: several pre-training steps are required
  * next sentence prediction, predict if sentence B is a next sentence of sentence A; bias model towards discourse
  * 50% the actual next sentence and in 50% a random sentence
* Trained on BooksCorpus (800M words) and English Wikipedia (2,500M words), sentence input length is 512 tokens
* Large training infrastrsucture, Cloud TPUs
* Fine-tuning for sentence tasks: take the hidden layer of the [CLS] token and add a liner classification layer; also fine-tune **all** BERT's weights
* Evaluation: GLUE datasets <https://gluebenchmark.com/faq> (test instances are on the server): The General Language Understanding Evaluation (GLUE) benchmark (Wang et al., 2018)
  * MNLI Multi-Genre Natural Language Inference: entailment, contradiction, neutral
  * QQP Quora Question Pairs: are two questions equivalent
  * QNLI Question Natural Language Inference (a version of Stanford Question Answering Dataset): question, answer --> correct, incorrect
  * SST-2 The Stanford Sentiment Treebank: movie reviews annotated for sentiment
  * CoLA The Corpus of Linguistic Acceptability: sentence --> acceptable / unacceptable
  * STS-B The Semantic Textual Similarity Benchmark: similarity of sentences / news headlines --> 1...5
  * MRPC Microsoft Research Paraphrase Corpus: sentences --> semnatically equivalent?
  * RTE Recognizing Textual Entailment
  * WNLI Winograd NLI
  * Both models of BERT outperform all existing systems on all tasks between 4,4% and 6.7%
* More evaluation
  * SQuAD v1.1: The Stanford Question Answering Dataset: Question sentence, Answer sentence --> span in the answer that contains the answer; for each word predict it is start or end of a span
  * CoNLL 2003 Named Entity Recognition: example of how to adopt token annotation to WordPiece tokens
  * SWAG The Situations with Adversarial Generations: sentence and 3 completions based on grounded videos; common sense reasoning; select the right completion; sentence is A and continuation B; predict the likelihood of the continuation
* Evaluations with ablation
  * No next sentence prediction: affects tasks that are based on cross-sentence relations QNLI, MNLI, SQuAD
  * Left-to-right-only and no-next sentence prediction: predict the next word as GPT, drop in performance accross all tasks
  * More parameters / larger models lead to increased performance
  * Masked language model converges slightly later (due to masking) than left-to-right-model but then afterwards an increase in performance is greater
* Using BERT as feature encoder
  * some tasks cannot be set-up as the previous classification tasks
  * computationally very cheap to use feature-encoders after training
  * extract activations of one or more layers on given input
  * best performance is achived by concatenating token representations of the last 4 hidden layers

Bender et al. 2021

* How big is too big?
* Environmental risks: energy required to train; environmental impacts on communities that don't benefit from LT
* Financial costs punishes marginalised communities: 90% of languages spoken by 1 billion communities have limited NLP resources
* Trained on only a selection of data prodiced by a community: amplify derogatory and stereotypical associations about gender, race, ethnicity and disability status; perpetuates dominant viewpoint, increasing power imbalances, inequality; In summary, LMs trained on large, uncurated, static datasets from the Web encode hegemonic views that are harmful to marginalized populations.
* Need to understand what is in the training data: curation and documentation
* To what degree large models do natural language understanding: are they onlt manipulating linguistic form
* Up to the end of Section 5, before Section 6: Stochastic parrots
