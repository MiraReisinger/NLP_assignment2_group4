# NLP_assignment2_group4
## Sentiment Role Labeling

The project *Traditional Semantic Role Labeling (SRL) system using explicit features* was carried out by [Elena Weber](https://github.com/elena-theresa-weber), [Alyssa Macgregor-Hastie](https://github.com/real-housewives-of-python), [Jiyun Sun](https://github.com/jiyunsun), and [Mira Reisinger](https://github.com/MiraReisinger) during the seminar ‘NLP Technology' as part of the Text Mining program 2021/2022 taught by Antske Fokkens and Pia Sommerauer at VU Amsterdam.

Semantic Role Labeling is about finding out who does what to whom using semantic representations within the sentences. The semantic roles indicate a relation among a predicate and its participants which is why the goal of the task is to identify and classify arguments of a given verb and assign them semantic labels that describe the roles they play in the predicate. 

## Data
The folder [**data**](https://github.com/MiraReisinger/NLP_assignment2_group4/tree/main/data) contains the annotated development, training, and test files from the Universal Propositon Banks Project for English and can also be found [here](<https://github.com/System-T/UniversalPropositions>). They are all in conll format. 

* `en_ewt-up-dev.conll` consists of 2000 sentences. 
* `en_ewt_up_train.conll` consists of 12543 sentences.
* `en_ewt_up_test.conll` consists of 2077 sentences.

The screenshot below shows the typical structure of the files with the annotations. The data starts with the sent_id, usually a link to the article, and the text, which is the complete sentence. The conll file itself has 10 main columns, with, among others, the token, the lemma, the POS, and the dependency. The 10th column is the predicate-sense label - if there is no predicate it is replaced with a *'_'*. The columns starting from 11 show the gold annotated arguments, depending on if a sentence only has one predicate then the row has 11 columns, if it has two predicates then it goes up to 12 columns, and so on. The sentence length varies greatly, thus there are several sentences with just one predicate and others with, for instance, four predicates. 
 
![Example structure data files](https://user-images.githubusercontent.com/90104896/157061220-27b6d9bc-626e-4be6-814f-747b16ae815a.png)

For part 2 of the assignment, [AllenNLP](https://github.com/allenai/allennlp) is used to train a neural LSTM classifier for Semantic Role Labeling. The following files are the preprocessed ones converting the conll SRL files into JSON. In the JSON file, each line is a sentence with a single predicate and its corresponding labeled arguments.

* `srl_univprop_en.dev.conllu.json`
* The results for the `train file` in part 2 can be found in a [Google Drive folder](https://drive.google.com/drive/folders/1wyRniTKswTNm-xAhq-awG9wBm8aKRAzF?usp=sharing) since the file is too big to upload to Github. 

## Code
To use this rule-based code for Semantic Role Labeling simply run `main.py` in your project terminal.

    example usage: `python main.py`

You can also run each file individually. 

    example usage: `python extract_features.py data/test_pred_arg.csv`

* `duplicate_sentences.py` This [code](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/duplicate_sentences.py) duplicates sentences that have more than one predicate as many times as there are predicates in them.

* `extract_pred_arg.py` This [code](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/extract_pred_arg.py) extracts the predicates and arguments and exports them as well as the tokens into a newly created csv file. Use this code for preprocessing the conll inputfiles.

* `extract_all_features.py` This [code](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/extract_all_features.py) generates all features to help the SVM classifier predict semantic roles. The input is the outputfile from `extract_pred_arg.py`. 

* `SVM.py` This [code](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/SVM.py)
 trains and runs a SVM classifer for Semantic Role Labling based on the outputs of `extract_features.py`. It will print a classification report in the terminal as well as a csv file with the report in the data folder.

* `main.py` This [code](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/main.py) runs the whole rule-based system.


To use the SRL with AllenNLP first run `conll_to_json.py` and then `srl_main.py`
* `conll_to_json.py` This [script](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/conll_to_json.py) takes in a ConLL file and converts it into a JSON format. The path of these converted  JSON files will be used as input for srl_main.py.

* `srl_main.py` This [script](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/srl_main.py) executes SRL by using an LSTM model trained on the Allen NLP library. 

`requirements.txt` The [requirements.txt](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/requirements.txt) shows the versions of the packages that are needed to run the scripts. For spaCy we strongly recommend using the version stated or at least a very similar one as newer versions created issues with the custom tokenizer. 

## Results
The following table provides an overview of the evaluation results of part 1: 

|              | precision   | recall      | f1-score    | support     |
|--------------|-------------|-------------|-------------|-------------|
| ARG0         | 0.807669959 | 0.802077323 | 0.804863926 | 1733        |
| ARG1         | 0.755232029 | 0.768281395 | 0.761700826 | 3241        |
| ARG1-DSP     | 1           | 0.25        | 0.4         | 4           |
| ARG2         | 0.561806656 | 0.627989371 | 0.593057298 | 1129        |
| ARG3         | 0.46875     | 0.202702703 | 0.283018868 | 74          |
| ARG4         | 0.454545455 | 0.178571429 | 0.256410256 | 56          |
| ARG5         | 0           | 0           | 0           | 1           |
| ARGA         | 0           | 0           | 0           | 2           |
| ARGM-ADJ     | 0.631178707 | 0.728070175 | 0.676171079 | 228         |
| ARGM-ADV     | 0.60625     | 0.586693548 | 0.596311475 | 496         |
| ARGM-CAU     | 0.393939394 | 0.282608696 | 0.329113924 | 46          |
| ARGM-COM     | 0           | 0           | 0           | 13          |
| ARGM-CXN     | 0.25        | 0.25        | 0.25        | 12          |
| ARGM-DIR     | 0.393939394 | 0.276595745 | 0.325       | 47          |
| ARGM-DIS     | 0.853658537 | 0.769230769 | 0.809248555 | 182         |
| ARGM-EXT     | 0.755555556 | 0.647619048 | 0.697435897 | 105         |
| ARGM-GOL     | 0.25        | 0.083333333 | 0.125       | 24          |
| ARGM-LOC     | 0.501901141 | 0.637681159 | 0.561702128 | 207         |
| ARGM-LVB     | 0.793103448 | 0.666666667 | 0.724409449 | 69          |
| ARGM-MNR     | 0.459016393 | 0.378378378 | 0.414814815 | 148         |
| ARGM-MOD     | 0.995454545 | 0.990950226 | 0.993197279 | 442         |
| ARGM-NEG     | 0.99537037  | 0.99537037  | 0.99537037  | 216         |
| ARGM-PRD     | 0.407407407 | 0.25        | 0.309859155 | 44          |
| ARGM-PRP     | 0.5         | 0.28        | 0.358974359 | 75          |
| ARGM-PRR     | 0.65        | 0.376811594 | 0.47706422  | 69          |
| ARGM-REC     | 0           | 0           | 0           | 0           |
| ARGM-TMP     | 0.832432432 | 0.850828729 | 0.841530055 | 543         |
| C-ARG0       | 0           | 0           | 0           | 3           |
| C-ARG1       | 0.56        | 0.269230769 | 0.363636364 | 52          |
| C-ARG1-DSP   | 0           | 0           | 0           | 1           |
| C-ARG2       | 0.357142857 | 0.714285714 | 0.476190476 | 7           |
| C-ARG3       | 0           | 0           | 0           | 2           |
| C-ARG4       | 0           | 0           | 0           | 0           |
| C-ARGM-CXN   | 0           | 0           | 0           | 5           |
| C-ARGM-LOC   | 0           | 0           | 0           | 1           |
| C-V          | 0.47826087  | 0.6875      | 0.564102564 | 16          |
| Gold         | 1           | 1           | 1           | 1           |
| R-ARG0       | 0.743902439 | 0.910447761 | 0.818791946 | 67          |
| R-ARG1       | 0.448717949 | 0.673076923 | 0.538461538 | 52          |
| R-ARG2       | 0           | 0           | 0           | 1           |
| R-ARG3       | 0           | 0           | 0           | 0           |
| R-ARGM-ADJ   | 0           | 0           | 0           | 1           |
| R-ARGM-ADV   | 0           | 0           | 0           | 1           |
| R-ARGM-DIR   | 0           | 0           | 0           | 1           |
| R-ARGM-LOC   | 0.727272727 | 0.888888889 | 0.8         | 9           |
| R-ARGM-MNR   | 0           | 0           | 0           | 8           |
| R-ARGM-TMP   | 0           | 0           | 0           | 2           |
| accuracy     | 0.726261128 | 0.726261128 | 0.726261128 | 0.726261128 |
| macro avg    | 0.396436346 | 0.362210441 | 0.364796528 | 9436        |
| weighted avg | 0.723250029 | 0.726261128 | 0.72183404  | 9436        |

# Answers Question 1 - 4 
## Predicate and Argument extraction 
1. *Extract predicates and arguments based on the dependency structure. Describe how you did this. Please note: Your approach is not going to be able to capture all predicates. If you have time left, you can replace your rule-based approach with a machine-learning-based approach.*

To extract the predicates and arguments based on the dependency structure the inputfile needs to be preprocessed first. After the file is being loaded the content is added to a default dictionary without the cells that are smaller than 2 and start with 'CopyOf'. Once the dictionary has been created a new file is being written that loops through the sentences and multiplies the sentence depending on the number of predicates within the sentence and adds the gold label arguments to column 11. Cells not containing a predicate are filled with an underscore. 
The items containing a hashtag or a star are being removed because they are not needed in the next steps. Once the items are removed it is being saved into a new conll file. Said file is read as a pandas dataframe with headers and in the following step the columns with the headers 'token', 'predicate', and 'argument' are saved in a new variable. This variable is saved as a csv file and used in the next steps of the assignment. 

In order to extract the predicates and arguments based on the dependency structure, we created the codes [duplicate_sentences.py](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/duplicate_sentences.py) and [extract_pred_arg.py](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/extract_pred_arg.py) that are used within the [main.py](https://github.com/MiraReisinger/NLP_assignment2_group4/blob/main/main.py).

## Classification task for argument classification
2. *Describe the classification task for argument classification. (You can decide whether you want to do this in one or in two steps.) Use your own words to describe what the classification instance is. You can refer to the background document for help.*

As stated above, the task Semantic Role Labeling focuses on detecting who does what to whom within a sentence. The roles indicate a relation within predicate and the arguments, or the predicates' participants, and can have different functions, like agent, the volitional causer of an event. The goal of the task is to identify and classify the arguments of the individual predicates and assign them semantic labels that give an indication about the position they have with predicates, meaning an output with labeled arguments. 

The pipeline goes as follows first the predicates have to be identified and classified, after that the arguments of the individual predicates can be detected based on said predicates. Afterward, the role labeling with the classifier, in our case the SVM, is being used to predict the arguments. 

## List of features 
3. *Make a list of features to extract (including but not limited to the syntactic dependency features extracted in Assignment 1). Add at least one lexical feature to your syntactic features (e.g. lemma, word embeddings). Describe all your features and explain why you chose them. You can check the literature in order to find out more about the features. You can also invent features yourself. Note: If you don’t manage to implement some of your features, please still include them in your list, but add a short comment stating that they are not implemented).*

TOKEN

We have selected the token as our lexical feature for this assignment. We have opted for word-tokenization (as opposed to character or sub-word tokenization) as it is more relevant to the purpose of argument identification and, in turn, argument classification.

POS-TAG

The POS-tag as a feature is essential for the task of argument classification. In linguistic terms, a predicate is a verb and an argument is generally a noun. Therefore, any token labeled as a verb is automatically classified as a predicate, whilst a token labeled as a noun can be considered to be an argument (depending on its relation to the predicate).

LEMMA

We selected the lemma as our lexical feature for this project. By lemmatizing a word and therefore removing morphological inflections, the resulting lemma could have less room for ambiguity and more accurate semantic detection. 

DEPENDENCY RELATION

In a similar way to POS-tags, dependency relations are vital for this specific task. By identifying the relation between tokens, we can accurately define which tokens are the most dependent on the head of the phrase, and therefore which ones can be classified as arguments.

HEAD OF DEPENDENCY

The “head” indicates the word on which the selected token is dependent. The identification of the head could result in the correct identification and extraction of a predicate and argument.

CONSTITUENT

Linguistically speaking, a constituent can be defined as part of a sentence. Constituents can be identified as noun phrases or verb phrases, with noun phrases typically containing the argument, and the verb phrases containing the predicate. The extraction and identification of the constituent is therefore essential for the task of argument classification.

PASSIVE TOKENS

This process identifies and extracts passive tokens within a dependency pipeline. If a token is identified as ‘passive’ the output is assigned a ‘True’ label, otherwise, it is assigned ‘False’. 
 
POSSIBLE ARGUMENT

The process for this feature involves identifying tokens with a “VERB” POS-tag and extracting the corresponding argument. As the data is not necessarily at a gold standard, there is a chance that some of the tokens are mislabelled as predicates, therefore it is not certain if the corresponding arguments are also correct. 

## Machine Learning Algorithm
4. *Select a machine learning algorithm. You can select any algorithm and use existing implementations (such as sklearn), but please motivate briefly why you chose it. A possible motivation is that it has been shown to work well in existing approaches (based on literature you read).*

In order to predict the arguments, we decided for the Support Vector Machine (SVM). SVM is a supervised machine learning model for classification and regression tasks. It distinguishes itself from other classifiers in the way that it creates a hyperplane to separate different categories. The hyperplane defines the maximum margin between the data points of each category, regularized by the C parameter that defines how much the classifier is ”allowed” to misclassify data points within the error margin. Related tasks and projects have also shown its effectiveness. 

