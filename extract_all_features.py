import sys
import pandas as pd
import spacy
from spacy.tokens import Doc
import csv


def extract_features(input_path, output_path):
    gold_a = []
    all_sentences = []
    sentence = []

    # read in file, extract tokens and gold labels
    with open(input_path, encoding='latin1') as infile:
        content = csv.reader(infile, delimiter='\t', quotechar='§')
        for row in content:  # create sentence list for spacy
            if row[0] == '':
                all_sentences.append(sentence)
                sentence = []
            else:
                sentence.append(row[0])
                gold_a.append(row[-1])

        def custom_tokenizer(text):
            '''create a customized tokenizer to scip tokenization in spacy pipeline and work based on tokens'''
            tokens = text
            return Doc(nlp.vocab, tokens)

        # create nlp for spacy out of tokens
        nlp = spacy.load("en_core_web_sm")
        nlp.tokenizer = custom_tokenizer

        data = []
        for sent in all_sentences:
            doc = nlp(sent, disable=['ner'])  # disable 'ner' to save time

            # possible dependency relations for arguments
            arg_dep = ['nsubj', 'dobj', 'nmod', 'amod', 'ccomp', 'xcomp' 'conj']

            # dependency pipeline
            for tok in doc:
                token = tok.text
                pos = tok.pos_
                lemma = tok.lemma_
                dependency = tok.dep_
                head = tok.head
                dependent = [t.text for t in tok.children]
                constituent = [t.text for t in tok.subtree]

                # find passive tokens - can we do the whole sentence gets passive label?
                cue = 'pass'
                if cue in dependency:
                    passive = True
                else:
                    passive = False

                # finding possible predicates and arguments
                if pos == 'VERB':
                    argument = 'V'
                elif dependency in arg_dep:
                    argument = 'ARG'
                else:
                    argument = '_'


                # crate dictionary for export
                feature_dict = {'Token': token, 'PoS': pos, 'Lemma': lemma, 'dependency': dependency, 'head': head,
                                'dependent': dependent,
                                'constituent': constituent, 'Passive': passive, 'possible_ARG': argument}
                data.append(feature_dict)

    
    # safe results with header to tsv file
    df = pd.DataFrame(data=data)
    df['Gold'] = gold_a  # append gold labels at the end
    df.to_csv(output_path, sep='\t', header=True, index=False)



def main(input_path=None):
    """Read in the inputfile, extract possible predicates, arguments and other features, write them to a file."""
    if not input_path:
        input_path = sys.argv[1]  # path to inputfile

        extract_features(input_path, input_path.replace('pred_arg.csv', 'all_features'))


if __name__ == '__main__':
    main()




