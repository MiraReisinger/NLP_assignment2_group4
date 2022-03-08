from numpy import extract
import pandas as pd 
import sys
###########################################
########## Extraction of Tokens, ##########
##########    Predicates, and    ##########
##########         Arguments     ##########
###########################################

def prepare_file(inputfile, output_path):
    '''
    this function prepares the preprocessed conll file and removes rows containing a '#' and '*' 
    :param inputfile: the inputfile is the path to the conll file that is going to be adapted
    :param output_path: the path for the outputfile in the format 'data/results/updated_file.conll' 
    '''
    to_be_removed = ['# newdoc id =', '# sent_id =','# text = ', '*'] 

    with open(inputfile, encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as newfile:
        for line in infile:
            if not any(to_be_removed in line for to_be_removed in to_be_removed):
                newfile.write(line)

def extract_pred_arg(inputfile_updated, output_path_second):
    '''
    the function adds headers to the inputfile and then extracts the columns containing 'token', 'predicate', and argument
    additionally empty cells are replaced with '_' 
    :param inputfile_updated: the input is the updated file created above 
    :param output_path_second: the parameter describes the path and name for the outputfile as a csv
    '''
    #creating headers
    header_gold = ["token_id", "token", "lemma", "pos", "pos again", "something", "dependency relation number", "dependency relation", "dependency + number", "Space:After", "predicate", "argument"] #,"argument1","argument2","argument3","argument4","argument5", 'argument6', 'argument7', 'argument8', 'argument9', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16', 'argument17', 'argument18', 'argument19', 'argument20', 'argument21', 'argument22', 'argument23', 'argument24', 'argument25', 'argument26', 'argument27', 'argument28', 'argument29', 'argument30', 'argument31', 'argument32', 'argument33', 'argument34']    
    #loading the file and adding headers
    conll_input = pd.read_csv(inputfile_updated, delimiter = '\t', names = header_gold, encoding = 'utf_8', quotechar = '§', engine='python')  
    #only extracting the column of tokens, predicates and arguments for outputfile 
    extracted_conll = conll_input[['token', 'predicate', 'argument']] 
    extracted_conll.fillna('_', inplace=True)
    #saving to a csv
    extracted_conll.to_csv(output_path_second, index = False, sep = '\t', quotechar = '§')


def main(argv = None):

    if argv is None:
        argv = sys.argv   # path to inputfile
 
    input_path = argv[1]
    output_path = argv[2]
    second_output_path = argv[3]

    prepare_file(input_path, output_path)
    extract_pred_arg(output_path, second_output_path)

if __name__ == '__main__':
    main()