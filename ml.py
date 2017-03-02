#!/usr/bin/python

import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression


def main():

    iris = datasets.load_iris()
    #print iris.data
    #print iris.target

    # load CSV data into numpy arr, ignoring CSV col
    train_data = np.genfromtxt('./stage_2/I.csv', delimiter=',')#[1:]
    train_data_nolabel = train_data[:, :4] # the data W/o the correct class. label
    train_data_target = train_data[:,4] # ONLY the correct classified label

    test_data = np.genfromtxt('./stage_2/J.csv', delimiter=',')#[1:]
    test_data_nolabel = test_data[:, :4] # the data W/o the correct class. label
    test_data_target = test_data[:,4] # ONLY the correct classified label



    #print (len(my_train_data_nolabel))
    #print (my_train_data_nolabel)
    #print (my_train_data_target)

    # "learn" from the training set, labeled, using
    # dt = decision tree
    # rf = random forest
    # svm = support vector machine
    # lin_r = linear regression
    # log_r = logarithmic regression
    classifiers = []

    clf_dt = tree.DecisionTreeClassifier()
    clf_dt = clf_dt.fit(train_data_nolabel, train_data_target)
    classifiers.append(clf_dt);

    clf_rf = RandomForestClassifier()
    clf_rf = clf_rf.fit(train_data_nolabel, train_data_target)
    classifiers.append(clf_rf);

    clf_svm = svm.SVC()
    clf_svm = clf_svm.fit(train_data_nolabel, train_data_target)
    classifiers.append(clf_svm);

    clf_lin_r = LinearRegression()
    clf_lin_r = clf_lin_r.fit(train_data_nolabel, train_data_target)
    #classifiers.append(clf_lin_r);

    clf_log_r = LogisticRegression()
    clf_log_r = clf_log_r.fit(train_data_nolabel, train_data_target)
    classifiers.append(clf_log_r);

    # save our P, R, and F1 values for each classifier.
    p_vals = [] # will be a list of P values
    r_vals = [] # will be a list of R values
    f1_vals = [] # will be a list of f1 values

    # test each classifier one by one
    for classifier in classifiers:
        pred = classifier.predict(test_data_nolabel);

        p = metrics.precision_score(test_data_target, pred);
        p_vals.append(p);

        r = metrics.recall_score(test_data_target, pred);
        r_vals.append(r);

        f1 = metrics.f1_score(test_data_target, pred);
        f1_vals.append(f1);



    print("clf: dt, rf, svm, log_r");
    print("P: ", p_vals);
    print("R: ", r_vals);
    print("F1: ", f1_vals);

                                  #p = metrics.precision_score(train_data_target, train_data_target)


if __name__ == "__main__":
    main();
