from sklearn.feature_extraction import DictVectorizer
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

import sys

### Parts of this code are based on an assignment for the course Machine Learning for NLP tought by Anstkse Fokkens at VU Amsterdam in 2021.

def extract_features_and_labels(trainingfile):
    '''Function that extracts features and gold labels from preprocessed file.
    :param trainingfile: path to the (preprocessed) csv file
    :return data: a list of dictionaries, with key-value pair providing the value for the feature `token' for individual instances
    :return gold: a list of gold labels of individual instances'''
    
    data = []
    gold = []
    
    with open(trainingfile, 'r', encoding='utf-8') as infile:
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
                gold_a = components[-1]
                feature_dict = {'Token': token, 'PoS': pos, 'Lemma': lemma, 'dependency': dependency, 'head': head,
                                'dependent': dependent, 'constituent': constituent, 'Passive': passive, 'possible_ARG': possible_ARG}
                data.append(feature_dict)
                gold.append(gold_a)
            
    return data, gold


def create_classifier(features, gold):
    ''' Function that takes feature-value pairs and gold labels as input and trains a SVM
   
    :param features: feature-value pairs
    :param labels: gold labels
    :type features: a list of dictionaries
    :type labels: a list of strings
    
    :return classifier: a trained SVM classifier
    :return vec: a DictVectorizer to which the feature values are fitted. '''
  
    model = LinearSVC()
    #model = LogisticRegression()
    vec = DictVectorizer()
    features_vectorized = vec.fit_transform(features)
    model.fit(features_vectorized, gold)

    return model, vec


def classify_data(model, vec, X_test, Y_test, testdata, outputfile):
    '''Function that creates predictions using SVM classifer and writes them out in a file
    
    :param model: trained classifer
    :param vec: vectorizer in which the mapping between feature values and dimensions is stored
    :param X_test: test instances
    :param Y_test: test gold labels
    :param testdata: path to the (preprocessed) test file
    :outputfile: path for outputfile   
    
    :return predictions: list of output labels provided by the classifier on the test file
    :return Y_test: list of gold labels as included in the test file
    
    '''

    features = vec.transform(X_test)
        
    predictions = model.predict(features)
    outfile = open(outputfile, 'w', encoding='utf-8')
    counter = 0

    for line in open(testdata, 'r', encoding='utf-8'):
        if len(line.rstrip('\n').split()) > 0:
            outfile.write(line.rstrip('\n') + '\t' + predictions[counter] + '\n')
            counter += 1
    outfile.close()

    return predictions, Y_test


def create_report(gold_labels, predictions):
    '''
    Function that creates precision, recall and f-score based on SVM classifer predictions
    
    :param predictions: predicted output by classifier
    :param goldlabels: original gold labels - Y_test
    '''
    report = classification_report(gold_labels,predictions)
    print('---------------SVM LINEAR Classifier Report-------------------')
    print('Features used: token, pos, lemma, dependency, head, dependent,\n constituent, passive_voice, possible_ARG, head_predicate')
    print()
    print(report)
    
def classification_report_csv(gold_labels, predictions):
    '''
    This function creates classification report as dictionary and exports it to a csv file in the data folder
    source: https://stackoverflow.com/questions/39662398/scikit-learn-output-metrics-classification-report-into-csv-tab-delimited-format
    '''
    clsf_report = pd.DataFrame(classification_report(y_true=gold_labels, y_pred=predictions, output_dict=True)).transpose()
    clsf_report.to_csv('data/classification_report.csv', index=True)


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
    predictions, gold_labels = classify_data(model, vec, X_test, Y_test, testfile, 'data/predictions.tsv')
    print('Predictions done - report will be created now')
    create_report(gold_labels, predictions)
    classification_report_csv(gold_labels, predictions)
    print('Main file Done')
    
    
if __name__ == '__main__':
    main()
