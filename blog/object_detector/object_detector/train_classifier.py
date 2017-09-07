# Import the required modules
from skimage.feature import local_binary_pattern
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import argparse as ap
import glob
import os
import numpy as np
from config import *
from sklearn import grid_search

if __name__ == "__main__":
    # Parse the command line arguments
    parser = ap.ArgumentParser()
    parser.add_argument('-p', "--posfeat", help="Path to the positive features directory", required=True)
    parser.add_argument('-n', "--negfeat", help="Path to the negative features directory", required=True)
    parser.add_argument('-c', "--classifier", help="Classifier to be used", default="LIN_SVM")
    args = vars(parser.parse_args())

    pos_feat_path =  args["posfeat"]
    neg_feat_path = args["negfeat"]

    # Classifiers supported
    clf_type = args['classifier']

    fds = []
    labels = []
    # Load the positive features
    for feat_path in glob.glob(os.path.join(pos_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(1)

    # Load the negative features
    for feat_path in glob.glob(os.path.join(neg_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(0)
    # print "here is feature"
    # print 'fds: {}--len list: {}'.format(fds[0], len(fds))
    # print "hear is label"
    # print 'labels: {}--len list: {}'.format(labels[0], len(labels))

    if clf_type is "LIN_SVM":
        clf = LinearSVC()
        ##clf = svm.SVC() np.array(list(fds), dtype=np.float)
        print "Training a Linear SVM Classifier"
        clf.fit(fds, labels)
        #clf.fit(list(np.array(fds)), labels)
        # define the parameter search space
        # search for the best classifier within the search space and return it

        # If feature directories don't exist, create them
        if not os.path.isdir(os.path.split(model_path)[0]):
            os.makedirs(os.path.split(model_path)[0])
        joblib.dump(clf, model_path)
        print "Classifier saved to {}".format(model_path)
