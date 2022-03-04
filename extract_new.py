import csv
import pandas as pd
from collections import defaultdict
import json

# inputpath of the file that needs to be extracted
inputfile = "data/en_ewt-up-dev.conll"


d = defaultdict(lambda:defaultdict(list))
current_sent = 0
with open(inputfile, encoding='utf-8') as infile:
    content = csv.reader(infile, delimiter = '\t', quotechar = '§')
    for row in content:
        if row == []:
            current_sent+=1
        elif row[0].startswith('#'):
            d[str(current_sent)]['sentence'].append(row)
            continue
        elif len(row) > 2 and row[9].startswith('CopyOf'):
            pass
        else: 
            d[str(current_sent)]['sentence'].append(row)
            if row[10] != "_":
                d[str(current_sent)]['predicate'].append(row[10])


### help from Rorick aka Aga and Doreen <3 
with open('data/dev_extracted.conllu', 'w', newline ='', encoding='utf-8') as csvfile:
    output = csv.writer(csvfile, delimiter = '\t')
    for sentences, values in d.items():
        if values['sentence'][0][0].startswith('# propbank'):
            continue
        else:
            for i, predicate in enumerate(values['predicate']):
                for sentence in values['sentence']:
                    # write non-token rows as original
                    if sentence[0].startswith('#'):
                        output.writerow(sentence)
                    
                    # write token rows with only one predicate and the correlating column of arguments
                    else:
                        new_row = sentence[:10] # all columns up till sense info, excluding sense info
                        if sentence[10] == predicate:
                            new_row.append(sentence[2]) # lemma, not sense
                        else:
                            new_row.append('_') # underscore for every other token that is not predicate
                        
                        new_row.append(sentence[11+i]) # arg info for predicate in question
                        output.writerow(new_row)

                output.writerow([])