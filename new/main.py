import os

######################
### Preprocessing ####
######################

## duplicating sentences
os.system("python duplicate_sentences.py data/en_ewt-up-dev.conll")
os.system("python duplicate_sentences.py data/en_ewt-up-train.conll")
os.system("python duplicate_sentences.py data/en_ewt-up-test.conll")

print('Duplicating sentences done')

## extract tokens, predicates and arguments
os.system("python extract_pred_arg.py data/en_ewt-up-dev_preprocessed.conll data/dev_updated")
os.system("python extract_pred_arg.py data/en_ewt-up-train_preprocessed.conll data/train_updated")
os.system("python extract_pred_arg.py data/en_ewt-up-test_preprocessed.conll data/test_updated")

print('Extract tokens, predicates and arguments done')

########################
### extract features ###
########################
# extract_features.py takes the output of extract tokens, predicate and argument as an argument and creates new file with all features
# this might take a while because of the size of the training file and SpaCy

os.system("python extract_all_features.py data/dev_pred_arg.csv")
os.system("python extract_all_features.py data/train_pred_arg.csv")
os.system("python extract_all_features.py data/test_pred_arg.csv")

print('Extract features done')

#######################################
### Train classifier and evaluation ###
#######################################
# first argument for SVM.py is trainingfile with all features, second is the testfile with all features
# This creates a file with the predictions and a report will be printed in the terminal

os.system("python SVM.py data/train_all_features data/test_all_features")

