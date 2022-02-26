import pandas as pd 

#inputpath of the file that needs to be extracted 
inputfile = "/data/srl_univprop_en.dev.conll"

#creating headers
header_gold = ["token_id", "token", "lemma", "pos", "pos again", "mood, number", "dependency relation number", "dependency relation", "dependency + number", "Space:After", "predicate", "argument"]    
 
#loading the file and adding headers
conll_input = pd.read_csv(inputfile, delimiter = '\t', names = header_gold, encoding = 'utf_8')

#only extracting the column of tokens, predicates and arguments for outputfile 
extracted_conll = conll_input[['token', 'predicate', 'argument']] 

#saving to a csv
extracted_conll.to_csv('data/dev_token_pred_arg.csv', sep = '\t')