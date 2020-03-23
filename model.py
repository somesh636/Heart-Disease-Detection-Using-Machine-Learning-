import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
#loading the iris data
d = pd.read_csv('heart.csv')
X=d.drop(['target'],axis=1)
y=d[['target']]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
rf=RandomForestClassifier(n_estimators=200,max_depth=3,random_state=42)
rf.fit(X_train,y_train.values.ravel())

pickle.dump(rf,open('model_pickle.pkl','wb'))