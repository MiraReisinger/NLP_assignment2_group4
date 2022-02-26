import sys
import pandas as pd
import spacy

def main(input_path=None):
    """Read in the inputfile, extract possible predicates, arguments and other features, write them to a file."""
    if not input_path:
        input_path = sys.argv[1]  # path to inputfile

    # read in file, extract tokens and gold labels
    conll_input = pd.read_csv(input_path, delimiter='\t', encoding='utf_8')
    tokens = conll_input['token']
    #gold_p = conll_input['predicate']
   # gold_a = conll_input['argument']

    # create nlp for spacy out of tokens
    document = ' '.join(tokens)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(document)
    sents = list(doc.sents)

    # possible dependency realtions for arguments
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
        base_dict = {'Token': token, 'PoS': pos, 'Lemma': lemma, 'dependency': dependency, 'head': head, 'dependent': dependent,
                     'constituent': constituent, 'Passive': passive ,'possible_ARG': argument, 'head-predicate': ancestors}
        data.append(base_dict)

    # safe results with header to tsv file
    df = pd.DataFrame(data=data)
    output_path = input_path.replace('.csv', '_prepro.tsv')
    df.to_csv(output_path, sep='\t', header=True, index=False)


if __name__ == '__main__':
    main()
