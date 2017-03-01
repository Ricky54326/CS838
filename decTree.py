import numpy as np
import csv
import pandas as pd
from sklearn import tree
from sklearn import datasets
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
filename = 'trainSet.csv'
names = ["article","quotation","numWords","capital","s","endOfSent","label"]
data = pd.read_csv(filename, names=names)
Xtrain = np.array(data[names[:-1]][1:]).astype(int)
Ytrain = np.array(data["label"][1:]).astype(int)
parameters = {'max_depth':range(3,10)}
clf = GridSearchCV(tree.DecisionTreeClassifier(), parameters, cv = 100, n_jobs=4)
clf.fit(Xtrain, Ytrain)
tree_model = clf.best_estimator_
print (clf.best_score_, clf.best_params_)