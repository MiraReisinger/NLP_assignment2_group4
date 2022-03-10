import csv
import sys

to_be_removed = ['# newdoc id =', '# sent_id =','# text = ', '*'] 

def prepare_file(inputfile, output_path):
    '''
    this function prepares the preprocessed conll file and removes rows containing a '#' and '*'
    :param inputfile: the inputfile is the path to the conll file that is going to be adapted
    :param output_path: the path for the outputfile in the format 'data/results/updated_file.conll'
    '''

    with open(inputfile, encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8')as newfile:
        for line in infile:
            if not any(to_be_removed in line for to_be_removed in to_be_removed):
                newfile.write(line)


def extract_pred_arg(inputfile_updated, outputfile):
    '''
    the function adds headers to the inputfile and then extracts the columns containing 'token', 'predicate', and argument
    additionally empty cells are replaced with '_'
    :param inputfile_updated: the input is the updated file created above
    :param output_path_second: the parameter describes the path and name for the outputfile as a csv
    '''

    tokens = []
    pred = []
    arg = []

    with open(inputfile_updated, encoding='utf-8') as csv_file:
        content = csv.reader(csv_file, delimiter='\t', quotechar='§')
        for row in content:
            if not row == []:
                tokens.append(row[1])
                pred.append(row[-2])
                arg.append(row[-1])
            elif row == []: # keep the empty lines
                tokens.append('')
                pred.append('')
                arg.append('')

    with open(outputfile, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter='\t', quotechar='§')
        for i in range(len(tokens)):
            content = [tokens[i], pred[i], arg[i]]
            writer.writerow(content)


def main(argv=None):
    if argv is None:
        argv = sys.argv  # path to inputfile

    input_path = argv[1]
    output_path = argv[2]

    prepare_file(input_path, output_path)
    extract_pred_arg(output_path, output_path.replace('updated', 'pred_arg.csv'))


if __name__ == '__main__':
    main()
