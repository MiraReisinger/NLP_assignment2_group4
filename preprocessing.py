import csv
from collections import defaultdict
import sys

#######################################
########## Preprocessing ##############
#######################################

def create_dictionary(input_path):
    '''
    this function creates a default dictionary out of the inputfile. additionally it skips over
    rows which length is below 2 and contain "CopyOf'. 
    :param input_path: the parameter is the inputpath to the file that should be preprocessed. the file needs to have 10 columns or more.
    :return dictionary_prepro: the function returns the default dictionary
    '''
    dictionary_prepro = defaultdict(lambda:defaultdict(list))
    current_sent = 0
    with open(input_path, encoding='utf-8') as infile:
        content = csv.reader(infile, delimiter = '\t', quotechar = '§')
        for row in content:
            if row == []:
                current_sent+=1
            elif row[0].startswith('#'):
                dictionary_prepro[str(current_sent)]['sentence'].append(row)
                continue
            elif len(row) > 2 and row[9].startswith('CopyOf'):
                pass
            else: 
                dictionary_prepro[str(current_sent)]['sentence'].append(row)
                if row[10] != "_":
                    dictionary_prepro[str(current_sent)]['predicate'].append(row[10])
    return dictionary_prepro

def write_file(dictionary_prepro, outputfile):
    '''
    the function creates a new file out of the above returned dictionary and multiplies the
    sentences by the number of predicates within the sentence in order to get access to all 
    the predicates and their arguments. 
    :param dictionary_prepro: the preprocessed dictionary created in the function create_dictionary
    :param outputfile: the filepath of the outputfile, e.g. 'data/results/train_preprocessed.conll'
    '''
    ### help from Rorick Terlou    
    with open(outputfile, 'w', newline ='', encoding='utf-8') as csvfile:
        output = csv.writer(csvfile, delimiter = '\t')
        for sentences, values in dictionary_prepro.items():
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

def main(argv = None):

    if argv is None:
        argv = sys.argv  # path to inputfile
 
    input_path = argv[1]
    
    dictionary_inputfile = create_dictionary(input_path)
    write_file(dictionary_inputfile, input_path.replace('.conll', '_preprocessed.conll'))

if __name__ == '__main__':
    main()