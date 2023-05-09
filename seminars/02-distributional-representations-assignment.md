# S2: Distributional representations

This assignment is a part of the preparation for the seminar on 13 April.

Please have a look [here](https://canvas.gu.se/courses/64394/pages/seminar-assignments-and-discussions) for how to prepare for the seminar.

In this seminar we will examine distributional representations of lexical meaning as modelled by vector space models and how these representations can be linked to *compositionality* of lexical items in phrases which we identified as one of the key properties of natural language. What do we mean by distributional meaning? How do we build vector space models computationally from corpora? How we generalise such representations? How we can compose the semantic vectors to get representations of phrases?

We will look at the following paper (or rather a chapter):

* S. Clark. [Vector space models of lexical meaning.](https://canvas.gu.se/courses/64394/files/7167380?wrap=1)


* [Download Vector space models of lexical meaning.](https://canvas.gu.se/courses/64394/files/7167380/download?download_frd=1) In S. Lappin and C. Fox, editors, Handbook of Contemporary Semantics — second edition, chapter 16, pages 493–522. Wiley – Blackwell, 2015.

Optional but helpful background and further reading:

* K. Erk. [Vector space models of word meaning and phrase meaning: A survey.](https://gu-se-primo.hosted.exlibrisgroup.com/permalink/f/15agpbr/TN_wj10.1002/lnco.362)


* [Links to an external site.](https://gu-se-primo.hosted.exlibrisgroup.com/permalink/f/15agpbr/TN_wj10.1002/lnco.362) Language and Linguistics Compass, 6(10):635–653, 2012.
* P. D. Turney, P. Pantel, et al. [From frequency to meaning: Vector space models of semantics.](http://dx.doi.org/10.1613/jair.2934)
* [Links to an external site.](http://dx.doi.org/10.1613/jair.2934) Journal of artificial intelligence research, 37(1):141–188, 2010.
* J. Mitchell and M. Lapata. [Vector-based models of semantic composition.](https://www.aclweb.org/anthology/P08-1028/)
* [Links to an external site.](https://www.aclweb.org/anthology/P08-1028/) In Proceedings of ACL-08: HLT, pages 236–244, Columbus, Ohio, 2008.
* J. Mitchell and M. Lapata. [Composition in distributional models of semantics.](http://dx.doi.org/10.1111/j.1551-6709.2010.01106.x)
* [Links to an external site.](http://dx.doi.org/10.1111/j.1551-6709.2010.01106.x)  Cognitive Science, 34(8):1388–1429, 2010.
* E. M. Bender and A. Koller. [Climbing towards NLU: On meaning, form, and understanding in the age of data.](https://www.aclweb.org/anthology/2020.acl-main.463)
* [Links to an external site.](https://www.aclweb.org/anthology/2020.acl-main.463) In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 5185–5198, Online, July 2020. Association for Computational Linguistics.
* S. Dobnik, R. Cooper, A. Ek, B. Noble, S. Larsson, N. Ilinykh, V. Maraev, and V. Somashekarappa. [In search of meaning and its representations for computational linguistics.](https://aclanthology.org/2022.clasp-1.4/)


* [Links to an external site.](https://aclanthology.org/2022.clasp-1.4/) In Proceedings of the 2022 CLASP Conference on (Dis)embodiment, pages 30–44, Gothenburg, Sweden, Sept. 2022. Association for Computational Linguistics.

The Clark chapter has two parts. The first part discusses the basics of the vector spaces; how they are built, evaluated and in what tasks they can be used for. The second part discusses one approach of combining a formal semantic grammar (Combinatory category grammar, CCG) and vector representations. You can think of CCG as lambda calculus. The proposal uses a dual system of composition: formal compositional rules over categories are matched with a distributional compositional rules that operate on distributional tensors/matrices.

The optional papers: (i) Erk and Turney and Pantel give a general overview of vector spaces. Mitchel and Lapata test different compositional functions for vectors and compare them to human judgements. Bender and Koller discuss limitations of using distributional representations for natural language processing. In our paper we discuss different representations of meaning used in natural language processing.

Below are some points that you may want to consider:

On vector space models:

* What notion of meaning is represented by distributional representations?
  * What semantic relations do they capture?
  * How do these relate to the semantic relations we intuitively recognise in natural language?
  * Are there relations that they do not capture?
  * Think of examples in natural language that can modelled well with distributional relations and examples that cannot be.
* How does this notion of meaning different from that taken in model-theoretic semantics that we looked at earlier?
  * Sense and reference?
* What are the main ... for representing meaning of natural language this way?
  * benefits
  * challenges
  * limitations (and dangers!)
* What computational resources, tools and methods do we use to create these representations?
* For what tasks can we use these representations? For what tasks we cannot use them?
* What would be alternative representations?

On compositionality:

* What are the reasons and benefits of combining formal representations with distributional ones?
* What do you think are the biggest challenges of such hybrid models and representations?
* To what degree can we interpret distributional representations?
  * How does this relate to how well a mapping between two types of representations can be achieved?
* There are several different ways to write a formal grammar. How would this affect the mapping?

The assignment is marked on a 7 level scale where 4 is sufficient to complete the assignment; 5 is good solid work; 6 is excellent work, covers most of the assignment; and 7: creative work that goes beyond the assignment.