
def data_preprocessing(df):
    #Dropping unnecessary columns
    df_updated = df.drop(['name','junk','Unnamed: 0'],axis=1)

    # Renaming num as target
    df_updated.rename(columns={'num':'target'}, inplace=True)
    df_updated[df_updated.columns[1:]].corr()['target'][:]
    df_updated.isnull().sum()
    df_updated.isna().sum()
    
    # Evaluating the count of each chol values
    df_updated['chol'].value_counts()

    # replacing 0 values of chol with its mean
    df_updated['chol'] = df_updated['chol'].replace(0, 191.82647385984427)

    # mapping 2,3,4 values to 1 in the target 
    df_updated['target'] = df_updated.target.map({0:0, 1:1, 2:1, 3:1, 4:1})

    standardScaler = StandardScaler()
    standardScaler.fit_transform(df_updated)

    data = df_updated[['age', 'sex', 'cp', 'chol', 'ladprox', 'laddist', 'cxmain', 'rcaprox', 'rcadist', 'om1', 'oldpeak', 'rldv5e', 'ramus', 'thalach', 'target']] 
    print("DATA: \n",data)

    X = data.drop(['target'],axis=1)
    print("X.shape: ",X.shape)
    print("Data.shape", data.shape)
    y = data['target']

    # split data train 80 % and test 20 %
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return x_train, x_test, y_train, y_test


def predict_classifier(classifier, x_test, y_test):
    acc = accuracy_score(y_test,classifier.predict(x_test))
    return acc 

if __name__ == "__main__":
    import os 
    import pickle
    import numpy as np
    import pandas as pd
    from sklearn.metrics import accuracy_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2

    pd.set_option('display.max_rows',None)
    pd.set_option('display.max_columns',None)
    
    # Reading heart disease dataset
    df = pd.read_csv('~/D_Drive/Projects/Python/aggregated.csv')
    x_train, x_test, y_train, y_test = data_preprocessing(df)
    #random forest classifier with n_estimators=10 (default)
    classifier = RandomForestClassifier(n_estimators = 10, random_state=42)

    # fitting the model
    classifier = classifier.fit(x_train,y_train)

    #testing of the model
    predict_value = classifier.predict(x_test)
    #acc = accuracy_score(y_test,classifier.predict(x_test))
    total_accuracy = predict_classifier(classifier, x_test, y_test)
    print("Accuracy is: ", total_accuracy)
    # #print("predict_value: ", predict_value)
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # dest = os.path.join(dir_path,'Pickle_Objects')
    # pickle.dump(classifier, open(os.path.join(dest, 'algorithm.pkl'), 'wb'), protocol=4)
