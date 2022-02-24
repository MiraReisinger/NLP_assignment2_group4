# NLP_assignment2_group4

The project was carried out by Elena Weber, Alyssa Macgregor-Hastie, Jiyun Sun and Mira Reisinger during the seminar ‘NLP Technology' taught by Antske Fokkens and Pia Sommerauer at VU Amsterdam.

## Data

## Code
* `xxxx` 
The goal of this code is to extract the predicates and arguments in a dataframe and can be saved as a tsv file. The output consists of the tokenized sentence, pos tags, dependency labels, head, dependent, children, argument and predicate. To get the predicate the pos tag was used to see which token is classified as a verb and it was tagged as V for labeling the predicate. For the arguments a list of the most common relations ('nsubj', 'dobj', 'nmod', 'amod', 'ccomp', 'xcomp' 'conj') was extracted and used to find those within the dataframe. Those were tagged with ARG.
## Resultsscree

# Answers Question 1 -5 
1. *Extract predicates and arguments based on the dependency structure. Describe how you did this. Please note: Your approach is not going to be able to capture all predicates. If you have time left, you can replace your rule-based approach with a machine-learning-based approach.*

Can be seen in code xxx 

2. *Describe the classification task for argument classification. (You can decide whether you want to do this in one or in two steps.) Use your own words to describe what the classification instance is. You can refer to the background document for help.*

3. *Make a list of features to extract (including but not limited to the syntactic dependency features extracted in Assignment 1). Add at least one lexical feature to your syntactic features (e.g. lemma, word embeddings). Describe all your features and explain why you chose them. You can check the literature in order to find out more about the features. You can also invent features yourself. Note: If you don’t manage to implement some of your features, please still include them in your list, but add a short comment stating that they are not implemented).*

1. TOKEN:
We have selected the token as our lexical feature for this assignment. We have opted for word-tokenization (as opposed to character or sub-word tokenization) as it is more relevant to the purpose of argument identification and, in turn, argument classification. 

2. PHRASE TYPE
Linguistically speaking, the phrase type (Noun Phrase or Verb Phrase) defines the syntactic property of the phrase expressing the semantic roles. In other words, the Noun Phrase (NP) contains the main argument(s) of the sentence, whilst the Verb Phrase (VP) contains the verb/predicate. 
    
3. POS-TAG
The POS-tag as a feature is essential for the task of argument classification. In linguistic terms, a predicate is a verb and an argument is generally a noun. Therefore, any token labelled as a verb is automatically classified as a predicate, whilst a token labelled as a noun can be considered to be an argument (depending on its relation to the predicate).

4. DEPENDENCY RELATION:
In a similar way to POS-tags, dependency relations are vital for this specific task. By identifying the relation between tokens, we can accurately define which tokens are the most dependent on the head of the phrase, and therefore which ones can be classified as arguments.

5. POSITION FEATURE:
As a general rule, the English language is structured in the S-V-O order (subject-verb-order). The position in which a token is established gives a great deal of information in regards to correctly classifying an argument. This feature can be represented as a binary value, e.g. if a token appears before a verb, it is assigned the value 0; if a token appears after a verb it is assigned the value 1.


4. *Select a machine learning algorithm. You can select any algorithm and use existing implementations (such as sklearn), but please motivate briefly why you chose it. A possible motivation is that it has been shown to work well in existing approaches (based on literature you read).*

5. *Generate training and test instances* 

