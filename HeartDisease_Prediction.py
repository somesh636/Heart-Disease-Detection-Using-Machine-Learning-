import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# set the customized settigs for pandas 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# get the data 
data_heart = pd.read_csv('~/D_Drive/Projects/WebApp/dataset/cleaveland.csv', header = None)
data_heart = data_heart.apply(pd.to_numeric, errors='coerce')
#print(data_heart)

#for DataFrame format for the library use
data_heart.columns = ['age', 'sex', 'cp', 'trestbps', 'chol',
                      'fbs', 'restecg', 'thalach', 'exang',
                      'oldpeak', 'slope', 'ca', 'thal', 'target']

data_heart.isnull().sum()

data_heart['target'] = data_heart.target.map({0:0, 1:1, 2:1, 3:1, 4:1})
data_heart['sex'] = data_heart.sex.map({0: 'female', 1: 'male'})
data_heart['thal'] = data_heart.thal.fillna(data_heart.thal.mean())
data_heart['ca'] = data_heart.ca.fillna(data_heart.ca.mean())

# distribution of target vs age 
sns.set_context("paper", font_scale = 2, rc = {"font.size": 20, "axes.titlesize": 25,"axes.labelsize": 20})
sns.catplot(kind = 'count', data = data_heart, x = 'age', hue = 'target', 
            order = data_heart['age'].sort_values().unique())
plt.title('Variation of Age for each target class')
plt.show(block = False)

# barplot of age vs sex 
sns.catplot(kind = 'bar', data = data_heart, hue = 'target', y = 'age', x = 'sex')
plt.title('Distribuiton of age vs sex with the target class')
plt.show(block = False)

data_heart['sex'] = data_heart.sex.map({'female':0, 'male' : 1 })


######### ------------------ DATA PREPROCESSING ---------------- #########
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split 

X = data_heart.iloc[:, :-1].values 
y = data_heart.iloc[:, -1].values 
#print for test
#print('X values:\n', X)
#print('Y values:\n' , y)
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.2, random_state = 0)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)
#print for test
#print('X_train: \n',X_train)
#print('X_test:\n', X_test)
#print('y_train: \n',y_train)
#print('y_test:\n', y_test)

# ********************** SVM and SV Classifier **************************************************************
from sklearn.svm import SVC 
from sklearn.metrics import confusion_matrix 
classifier = SVC(kernel = 'rbf')
classifier.fit(X_train, y_train)

# prediction of the results

y_results = classifier.predict(X_test)
mat_test = confusion_matrix(y_results, y_test)

# confsion matrix for measuring algorithm efficiency output of a 
#  classifier on the dataset 
#  link (https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html)

y_pred_train = classifier.predict(X_train)
confusion_matrix_train = confusion_matrix(y_pred_train, y_train) 

print('****************************************************************************')
print('* --> Accuracy of the training set for svm = {}'.format((confusion_matrix_train[0][0] + confusion_matrix_train[1][1])/len(y_train)))
print('* --> Accuracy of the test dataset for the svm = {}'.format((mat_test[0][0] + mat_test[1][1])/len(y_test)))
print('****************************************************************************')


# ================== LOGISTIC REGRESSION ============================ 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix 

X = data_heart.iloc[:, :-1].values 
y = data_heart.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0)

classifier_linear = LogisticRegression()
classifier_linear.fit(X_train, y_train)

y_logistic_results = classifier_linear.predict(X_test)

#confusion matrix train and test
confusion_matrix_Ltest = confusion_matrix(y_logistic_results,y_test)

#train confusion 

LG_y_train = classifier_linear.predict(X_train)
confusion_matrix_Ltrain = confusion_matrix(LG_y_train, y_train)

print('****************************************************************************')
print('* --> Accuracy of the traing dataset for LR is: {}'.format((confusion_matrix_Ltrain[0][0] + confusion_matrix_Ltrain[1][1])/len(y_train)))
print('* --> Accuracy of the testing dataset for the LR is: {}'.format((confusion_matrix_Ltest[0][0] + confusion_matrix_Ltest[1][1])/len(y_test)))
print('****************************************************************************')