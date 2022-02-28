import sys
import pandas as pd
import spacy
from spacy.tokens import Doc
import csv

def main(input_path=None):
    """Read in the inputfile, extract possible predicates, arguments and other features, write them to a file."""
    if not input_path:
        input_path = sys.argv[1]  # path to inputfile

    # read in file, extract tokens and gold labels
    content = pd.read_csv(input_path, encoding='utf_8')
    tokens = content['token']
    #gold_p = content['predicate']
    gold_a = content['argument']

    # create nlp for spacy out of tokens
    nlp = spacy.load("en_core_web_sm")

    def custom_tokenizer(text):
        '''create a customized tokenizer to scip tokenization in spacy pipeline and work based on tokens'''
        token = text.tolist()
        return Doc(nlp.vocab, token)

    nlp.tokenizer = custom_tokenizer
    doc = nlp(tokens)
    #sents = list(doc.sents)

    # possible dependency relations for arguments
    arg_dep = ['nsubj', 'dobj', 'nmod', 'amod', 'ccomp', 'xcomp' 'conj']

    data = []

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

        # finding corresponding predicate to ARG
        ancestors = []
        if argument == 'ARG':
            for ancestor in tok.ancestors:
                if ancestor.pos_ == 'VERB':
                    ancestors.append(ancestor)
                    break

        # crate dictionary for export
        feature_dict = {'Token': token, 'PoS': pos, 'Lemma': lemma, 'dependency': dependency, 'head': head, 'dependent': dependent,
                     'constituent': constituent, 'Passive': passive ,'possible_ARG': argument, 'head-predicate': ancestors}
        data.append(feature_dict)


    # safe results with header to tsv file
    df = pd.DataFrame(data=data)
    df['Gold'] = gold_a # append gold labels at the end
    output_path = 'data/all_features.tsv'
    df.to_csv(output_path, sep='\t', header=True, index=False)

if __name__ == '__main__':
    main()




