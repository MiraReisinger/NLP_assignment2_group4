import pandas as pd 

#inputpath of the file that needs to be extracted 
inputfile = "/data/srl_univprop_en.dev.conll"

to_be_removed = ['# newdoc id =', '# sent_id =','# text = ', '*'] 
#to_be_replaced = ['*']

with open(inputfile, encoding='utf-8') as infile, open('data/updated_file.conll', 'w', encoding='utf-8')as newfile:
    for line in infile:
        if not any(to_be_removed in line for to_be_removed in to_be_removed):
            newfile.write(line)

inputfile_updated =  "/data/updated_file.conll"

#creating headers
header_gold = ["token_id", "token", "lemma", "pos", "pos again", "mood, number", "dependency relation number", "dependency relation", "dependency + number", "Space:After", "predicate", "argument"]    
 
#loading the file and adding headers
conll_input = pd.read_csv(inputfile, delimiter = '\t', names = header_gold, encoding = 'utf_8')

#only extracting the column of tokens, predicates and arguments for outputfile 
extracted_conll = conll_input[['token', 'predicate', 'argument']] 

#saving to a csv
extracted_conll.to_csv('data/dev_token_pred_arg.csv', sep = ',')
