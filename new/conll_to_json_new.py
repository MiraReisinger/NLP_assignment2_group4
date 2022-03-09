import re, csv
import json

def conll_to_json(conll_file):

infos = {}
num = 0
with open(conll_file, encoding='utf-8') as fr:
    for line in fr:
        if line.startswith("#"):
            pass
        else:
            nl = line.strip().split()
            if len(nl)==0:
                num+=1
                infos.setdefault(num, [])
            else:
                infos.setdefault(num, []).append(nl)
                
#Write new json file - in this case, we are converting the training data

fw = open('srl_univprop_en.train.conllu.json', 'w', encoding='utf-8')

for k, v in infos.items():
    #print(k)
    seq_words = []
    BIO = []
    pred_sense = []
    
# Add tokens to the 'seq_words' list

    for vv in v:
        seq_words.append(vv[1])

# Add BIO tags to the 'BIO'list
        try:
            if vv[11] != '_':
                BIO.append('B-'+vv[11])
            else:
                BIO.append('O')
        except:
            pass
        
# Ensure that 'seq_words' and 'BIO lists' are the same length
#Taken from  https://stackoverflow.com/questions/43336837/making-equal-size-lists-in-python
        arrays=[seq_words,BIO]
        max_length=0
        for array in arrays:
            max_length=max(max_length,len(array))
        for array in arrays:
            array += ['O']*(max_length - len(array))

    ds = {"seq_words":seq_words, "BIO":BIO, "pred_sense":[]}

# Add the verb tenses to the 'pred_sense' list
    for qq in v:
        if (qq[3] in ['VERB'])  or (qq[3] in ['AUX'] and qq[4] in ['VBZ','VBD','VBN']):
            try:
                ds['pred_sense'] = [int(qq[0])-1, qq[10], qq[11], qq[4]]

            except:
                pass

#Check that the 'BIO' 'seq_words' lists are equal length

            for aa in ds.keys():
                if len(seq_words)!= len(BIO):
                    print(seq_words)
                    print(BIO)
                    print('------------------')
                else:
                    pass
            print(k, ds)

            fw.write(json.dumps(ds, ensure_ascii=False)+'\n')
            fw.flush()
        else:
            pass
fw.close()
