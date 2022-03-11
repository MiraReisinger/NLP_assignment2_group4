# NLP_assignment2_group4
## Sentiment Role Labeling

The project *Traditional Semantic Role Labeling (SRL) system using explicit features* was carried out by [Elena Weber](https://github.com/elena-theresa-weber), [Alyssa Macgregor-Hastie](https://github.com/real-housewives-of-python), [Jiyun Sun](https://github.com/jiyunsun), and [Mira Reisinger](https://github.com/MiraReisinger) during the seminar ‘NLP Technology' as part of the Text Mining program 2021/2022 taught by Antske Fokkens and Pia Sommerauer at VU Amsterdam.

## Data
The folder [**data**](https://github.com/MiraReisinger/NLP_assignment2_group4/tree/main/data) contains the annotated development, training and test files from the Universal Propositon Banks Project for English and can also be found [here](<https://github.com/System-T/UniversalPropositions>). They are all in conll format. 

* `en_ewt-up-dev.conll` consists of 2000 sentences. 
* `en_ewt_up_train.conll` consists of 12543 sentences.
* `en_ewt_up_test.conll` consists of 2077 sentences.

The screenshot below shows the typical structure of the files with the annotations. The data starts with the sent_id, usually a link to the article, and the text, which is the complete sentence. The conll file itself has 10 main columns, with, among others, the token, the lemma, the POS, and the dependency. The 10th column is the predicate-sense label - if there is no predicate it is replaced with a *'_'*. The columns starting from 11 shows the gold annotated arguments, depending if a sentence only has one predicate then the row has 11 columns, if it has two predicates then it goes up to 12 columns and so on. The sentence length varies greatly, thus there are several sentences with just one predicate and other with, for instance, four predicates. 
 
![Example structure data files](https://user-images.githubusercontent.com/90104896/157061220-27b6d9bc-626e-4be6-814f-747b16ae815a.png)


## Code
---------------------------needs to be updated---------------------------------------------------------
------------- also say something about spacy issue to recommend the version we have been using ---- 
* `extract_pred_arg.py` This code extracts the predicates and arguments and exports them as well as the tokens into a newly created csv file. Use this code for preprocessing the conll inputfiles. Use for both training- and testfile. HOW TO RUN IT?
* `extract_features.py` This code generates all features to help the SVM classifier predict semantic roles. The input is the outputfile from `extract_pred_arg.py` for both training- and testfile. The script needs to be called from the command line, passing it the path to inputfile.
    
    example usage:
    `python extract_features.py data/prepro_train.csv`
    
* `SVM.py` This codes traines and runs a SVM classifer for Semantic role Labling based on the outputs of `extract_features.py`. Usage is the same as `extract_features.py`

## Results
![results_v1](https://user-images.githubusercontent.com/67761190/156067192-7b4b1449-53c3-41cd-8c81-635f532cea44.PNG)


# Answers Question 1 -5 
----------------------------------------------needs to be updated--------------------------------------------------------------------
## Predicate and Argument extraction 
1. *Extract predicates and arguments based on the dependency structure. Describe how you did this. Please note: Your approach is not going to be able to capture all predicates. If you have time left, you can replace your rule-based approach with a machine-learning-based approach.*

To extract the predicates and arguments based on the dependency structure the inputfile needs to be preprocessed first. After the file is being loaded the content is added to a default dictionary without the cells that are smaller than 2 and start with 'CopyOf'. Once the dictionary has been created a new file is being written that loops through the sentences and multiplies the sentence depending on the number of predicates within the sentence and adding the gold label arguments to column 11. Cells not containing a predicate are filled with an underscore. 
The items containing a hashtag or a star are being removed because they are not needed in the next steps. Once the items are removed it is being saved into a new conll file. Said file is read as a pandas dataframe with headers and in the following step the columns with the headers 'token', 'predicate', and 'argument' are saved in a new variable. This variable is saved as a csv file and used in the next steps of the assignment. 

## Classification task for argument classification
2. *Describe the classification task for argument classification. (You can decide whether you want to do this in one or in two steps.) Use your own words to describe what the classification instance is. You can refer to the background document for help.*

## List of features 
3. *Make a list of features to extract (including but not limited to the syntactic dependency features extracted in Assignment 1). Add at least one lexical feature to your syntactic features (e.g. lemma, word embeddings). Describe all your features and explain why you chose them. You can check the literature in order to find out more about the features. You can also invent features yourself. Note: If you don’t manage to implement some of your features, please still include them in your list, but add a short comment stating that they are not implemented).*

TOKEN

We have selected the token as our lexical feature for this assignment. We have opted for word-tokenization (as opposed to character or sub-word tokenization) as it is more relevant to the purpose of argument identification and, in turn, argument classification. 
    
POS-TAG

The POS-tag as a feature is essential for the task of argument classification. In linguistic terms, a predicate is a verb and an argument is generally a noun. Therefore, any token labelled as a verb is automatically classified as a predicate, whilst a token labelled as a noun can be considered to be an argument (depending on its relation to the predicate).

LEMMA

DEPENDENCY RELATION

In a similar way to POS-tags, dependency relations are vital for this specific task. By identifying the relation between tokens, we can accurately define which tokens are the most dependent on the head of the phrase, and therefore which ones can be classified as arguments.

HEAD OF DEPENDENCY

CONSTITUENT 

PASSIVE TOKENS

POSSIBLE ARGUMENT

## Machine Learning Algorithm
4. *Select a machine learning algorithm. You can select any algorithm and use existing implementations (such as sklearn), but please motivate briefly why you chose it. A possible motivation is that it has been shown to work well in existing approaches (based on literature you read).*

The core classifier we are going to make prediction is the Support Vector Machine (SVM), a supervised machine learning model for classification and regression tasks. An SVM distinguishes itself from other classifiers in the way that it creates a hyperplane to separate different categories. The hyperplane defines the maximum margin between the data points of each category, regularized by the C parameter that defines how much the classifier is ”allowed” to misclassify data points within the error margin. And we also made more practives before about this classifier, so we decided to make prediction with this classifier.

## Training and test instances
5. *Generate training and test instances* 

