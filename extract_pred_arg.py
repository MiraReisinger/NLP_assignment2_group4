import sys
import pandas as pd
import spacy

def main(input_path=None):
    """Read in the inputfile, extract predicates and possible arguments write them to a file."""
    if not input_path:
        input_path = sys.argv[1]  # path to file to analyze

    data = []
    sentences = []
    # read in file, extract whole sentences
    with open(input_path, 'r') as infile:
        for line in infile:
            components = line.rstrip('\n').split()

            if line.startswith('# text ='):
                sent = line.strip('# text = ')
                senten = sent.strip()
                sentences.append(senten)

    # create text out of sentences
    nlp = spacy.load("en_core_web_sm")
    text = ''.join(sentences)
    doc = nlp(text)

    #possible dependency realtions for arguments
    arg_dep = ['nsubj', 'dobj', 'nmod', 'amod', 'ccomp', 'xcomp' 'conj']

    # dependency pipeline
    for tok in doc:
        token = tok.text
        pos = tok.pos_
        dependency = tok.dep_
        head = tok.head
        dependent = [t.text for t in tok.children]
        constituent = [t.text for t in tok.subtree]

        #finding possible predicates and arguments
        if pos == 'VERB':
            argument = 'V'

        elif dependency in arg_dep:
            argument = 'ARG'
        else:
            argument = '_'

        # finding corresponding predicate
        ancestors = []
        if argument == 'ARG':
            for ancestor in tok.ancestors:
                if ancestor.pos_ == 'VERB':
                    ancestors.append(ancestor)
                    break

        # crate dictionary for export
        base_dict = {'Token': token, 'POS': pos, 'dependency': dependency, 'head': head, 'dependent': dependent,
                     'constituent': constituent, 'argument': argument, 'predicate': ancestors}
        data.append(base_dict)

    # safe results with header to tsv file
    df = pd.DataFrame(data=data)
    output_path = input_path.replace('.conll', '_pred_arg.txt')
    df.to_csv(output_path, sep='\t', header=True, index=False)

if __name__ == '__main__':
    main()
