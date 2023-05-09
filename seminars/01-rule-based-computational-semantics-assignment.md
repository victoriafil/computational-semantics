# S1: Rule-based computational semantics

This assignment is a part of the preparation for the seminar on 30 March.

Please have a look [here](https://canvas.gu.se/courses/64394/pages/seminar-assignments-and-discussions) for how to prepare for the seminar.

In this seminar we will look at the key issues related to using logic for representing natural language semantics: how we translate natural language to different kinds of logic representations, ensure compositionality of linguistic expressions, how we can use these representations to evaluate what sentences mean, deal with ambiguity of natural language and finally how we can draw inference with semantic representations. 

In this seminar we will look at the following paper (or rather a chapter):

* [Chapter 10: Analyzing the meaning of sentencesLinks to an external site.](https://www.nltk.org/book/ch10.html) of S. Bird, E. Klein, and E. Loper. Natural language processing with Python. O’Reilly, 2009. (You may leave out section 5 Discourse semantics).

Optional but helpful background:

* M. Stone. [Semantics and computation.Links to an external site.](https://www.cs.rutgers.edu/~mdstone/pubs/compsem13.pdf) In M. Aloni and P. Dekker, editors, The Cambridge Handbook of Formal Semantics, Cambridge Handbooks in Language and Linguistics, chapter 25, pages 775–800. Cambridge University Press, Cambridge, UK, July 2016.

The chapter gives an overview of key questions related to implementing logic-based models and provides examples of implementations in Python and feature-based unification grammars. If you are new to this topic, you might find the chapter quite dense. However, do not despair! The purpose of the seminar is to familiarise yourself with these and but also to critically discuss what features of natural language meaning we represent this way, what are useful applications of this approach and its limitations. In the programming assignment (which follows this assignment) we will practically implement some extensions of the models and grammars presented here. 

Below are some points that you may want to consider when reading these papers:

* What are challenges of translating natural language to logic (in general)?
* Logics are formal languages each with specific properties: what aspects of natural language semantics are treated well with logic and what aspects are not captured?
* How is underspecification of quantifier scope implemented in Cooper storage?
* How about other forms of underspecification in natural language, e.g. lexical ambiguity?
* Why do we need lambda calculus?
* How can we use model builders and theorem provers (computational tools) to check validity of arguments?
* Do humans also reason logically - do they make the same inferences as theorem provers and model builders?
* In what NLP applications we would use this approach?

The assignment is marked on a 7 level scale where 4 is sufficient to complete the assignment; 5 is good solid work; 6 is excellent work, covers most of the assignment; and 7: creative work that goes beyond the assignment.