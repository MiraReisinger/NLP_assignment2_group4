from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
import sys

def extract_features_and_labels(trainingfile):
    '''XXXXX'''
    data = []
    gold = []
    with open(trainingfile, 'r', encoding='utf8') as infile:
        for line in infile:
            components = line.rstrip('\n').split()
            if len(components) > 0:
                token = components[0]
                pos = components[1]
                lemma = components[2]
                dependency = components[3]
                head = components[4]
                dependent = components[5]
                constituent = components[6]
                passive = components[7]
                possible_ARG = components[8]
                head_predicate = components[9]
                gold_a = components[-1]
                feature_dict = {'Token':token, 'POS': pos, 'lemma': lemma, 'dependency': dependency, 'head': head, 'dependent': dependent,
                'constituent': constituent, 'passive': passive, 'possible ARG': possible_ARG, 'head predicate': head_predicate}
                data.append(feature_dict)
                gold.append(gold_a)
            
    return data, gold


def create_classifier(features, gold):
    '''XXXXXX'''
  
    model = LinearSVC(max_iter = 1000)
    vec = DictVectorizer()
    features_vectorized = vec.fit_transform(features)
    model.fit(features_vectorized, gold)

    return model, vec


def classify_data(model, vec, X_test, Y_test, testdata, outputfile):
    '''XXXXXX'''

    features = vec.transform(X_test)
        
    predictions = model.predict(features)
    outfile = open(outputfile, 'w')
    counter = 0
    for line in open(testdata, 'r'):
        if len(line.rstrip('\n').split()) > 0:
            outfile.write(line.rstrip('\n') + '\t' + predictions[counter] + '\n')
            counter += 1
    outfile.close()
    return predictions, Y_test



def create_report(gold_labels, predictions):
    '''XXXXX'''
#### this report gives the results for the classifier
    report = classification_report(gold_labels,predictions)
    print('---------------SVM LINEAR Classifier Report-------------------')
    print('Features used: token, pos, lemma, dependency, head, dependent,\n constituent, passive_voice, possible_ARG, head_predicate')
    print()
    print(report)


def main(trainingfile=None, testfile=None):
    """Read in training and testfile, train SVM classifier, write predictions to a file."""
    if not trainingfile:
        trainingfile = sys.argv[1] # path to trainingsfile
    if not testfile:
        testfile = sys.argv[2] # path to testfile

    # create instances for classifier
    X_train, Y_train = extract_features_and_labels(trainingfile)
    X_test, Y_test = extract_features_and_labels(testfile)

    # create classifier and report
    model, vec = create_classifier(X_train, Y_train)
    predictions, gold_labels = classify_data(model, vec, X_test, Y_test, testfile, 'predictions.tsv')
    create_report(gold_labels, predictions)

if __name__ == '__main__':
    main()