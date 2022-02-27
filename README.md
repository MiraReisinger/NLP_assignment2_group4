# NLP_assignment2_group4

The project was carried out by Elena Weber, Alyssa Macgregor-Hastie, Jiyun Sun and Mira Reisinger during the seminar ‘NLP Technology' taught by Antske Fokkens and Pia Sommerauer at VU Amsterdam.

## Data

## Code
* `extract_pred_arg.py` This code extracts the predicates and arguments and exports them as well as the tokens into a newly created csv file. 

## Resultsscreen

# Answers Question 1 -5 
1. *Extract predicates and arguments based on the dependency structure. Describe how you did this. Please note: Your approach is not going to be able to capture all predicates. If you have time left, you can replace your rule-based approach with a machine-learning-based approach.*

The inputfile is being loaded and preprocessed by removing items containing a hashtag or a star. Once the items are removed it is being saved into a new conll file called 'updated_file.conll'. Said file is read as a pandas dataframe with headers and in the following step the columns with the headers 'token', 'predicate', and 'argument'are saved in a new variable. This variable is saved as a csv file and used in the next steps of the assignment. 

2. *Describe the classification task for argument classification. (You can decide whether you want to do this in one or in two steps.) Use your own words to describe what the classification instance is. You can refer to the background document for help.*

3. *Make a list of features to extract (including but not limited to the syntactic dependency features extracted in Assignment 1). Add at least one lexical feature to your syntactic features (e.g. lemma, word embeddings). Describe all your features and explain why you chose them. You can check the literature in order to find out more about the features. You can also invent features yourself. Note: If you don’t manage to implement some of your features, please still include them in your list, but add a short comment stating that they are not implemented).*

TOKEN:
We have selected the token as our lexical feature for this assignment. We have opted for word-tokenization (as opposed to character or sub-word tokenization) as it is more relevant to the purpose of argument identification and, in turn, argument classification. 

PHRASE TYPE
Linguistically speaking, the phrase type (Noun Phrase or Verb Phrase) defines the syntactic property of the phrase expressing the semantic roles. In other words, the Noun Phrase (NP) contains the main argument(s) of the sentence, whilst the Verb Phrase (VP) contains the verb/predicate. 
    
POS-TAG
The POS-tag as a feature is essential for the task of argument classification. In linguistic terms, a predicate is a verb and an argument is generally a noun. Therefore, any token labelled as a verb is automatically classified as a predicate, whilst a token labelled as a noun can be considered to be an argument (depending on its relation to the predicate).

DEPENDENCY RELATION:
In a similar way to POS-tags, dependency relations are vital for this specific task. By identifying the relation between tokens, we can accurately define which tokens are the most dependent on the head of the phrase, and therefore which ones can be classified as arguments.

POSITION FEATURE:
As a general rule, the English language is structured in the S-V-O order (subject-verb-order). The position in which a token is established gives a great deal of information in regards to correctly classifying an argument. This feature can be represented as a binary value, e.g. if a token appears before a verb, it is assigned the value 0; if a token appears after a verb it is assigned the value 1.

4. *Select a machine learning algorithm. You can select any algorithm and use existing implementations (such as sklearn), but please motivate briefly why you chose it. A possible motivation is that it has been shown to work well in existing approaches (based on literature you read).*

The main classifier we opted to use is the Support Vector Machine (SVM), a supervised learning model for classification and regression tasks. An SVM distinguishes itself from other classifiers in the way that it creates a hyperplane to distinctly separate different categories. The hyperplane defines the maximum margin between the data points of each category, regularized by the C parameter that defines how much the classifier is ”allowed” to misclassify data points within the error margin.

5. *Generate training and test instances* 

