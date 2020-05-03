import pandas as pd
import numpy as np
import settings

a = np.array([1,1,1,1,1,1,1,1,1,1,1,1],dtype='int')

def makePrediction(a):
    # import matplotlib.pyplot as plt
    # import seaborn as sns

    from sklearn.linear_model import LogisticRegression

    mental_health_train = pd.read_csv("survey.csv");


    # prep
    from sklearn.model_selection import train_test_split
    from sklearn import preprocessing
    from sklearn.datasets import make_classification
    from sklearn.preprocessing import binarize, LabelEncoder, MinMaxScaler

    # models
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier

    # Validation libraries
    from sklearn import metrics
    from sklearn.metrics import accuracy_score, mean_squared_error, precision_recall_curve
    from sklearn.model_selection import cross_val_score


    from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
    from sklearn.neighbors import KNeighborsClassifier

    mental_health_train

    mental_health_train.isnull().sum()

    mental_health_train.drop('Timestamp',axis = 1,inplace = True)


    mental_health_train.drop('state',axis = 1,inplace = True)


    mental_health_train.drop('no_employees',axis = 1,inplace = True)
    mental_health_train.drop('phys_health_consequence',axis = 1,inplace = True)
    mental_health_train.drop('coworkers',axis = 1,inplace = True)
    mental_health_train.drop('supervisor',axis = 1,inplace = True)
    mental_health_train.drop('mental_health_interview',axis = 1,inplace = True)
    mental_health_train.drop('Country',axis = 1,inplace = True)


    mental_health_train

    mental_health_train.drop('phys_health_interview',axis = 1,inplace = True)
    mental_health_train.drop('mental_vs_physical',axis = 1,inplace = True)
    mental_health_train.drop('obs_consequence',axis = 1,inplace = True)
    mental_health_train.drop('comments',axis = 1,inplace = True)

    mental_health_train


    mental_health_train.isnull().sum()

    def self_employed(cols):
        self = cols['self_employed'];
        if pd.isnull(self):
            return 'No'
        else:
            return self

    mental_health_train['self_employed'] = mental_health_train[['self_employed']].apply(self_employed,axis=1)

    #sns.heatmap(mental_health_train.isnull())

    mental_health_train.drop('work_interfere',axis = 1,inplace = True)

    mental_health_train.drop('leave',axis = 1,inplace = True)

    #sns.heatmap(mental_health_train.isnull())

    mental_health_train.shape

    mental_health_train

    mental_health_train.Gender.unique()

    male_str = ["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man","msle", "mail", "malr","cis man", "Cis Male", "cis male"]
    trans_str = ["trans-female", "something kinda male?", "queer/she/they", "non-binary","nah", "all", "enby", "fluid", "genderqueer", "androgyne", "agender", "male leaning androgynous", "guy (-ish) ^_^", "trans woman", "neuter", "female (trans)", "queer", "ostensibly male, unsure what that really means"]           
    female_str = ["cis female", "f", "female", "woman",  "femake", "female ","cis-female/femme", "female (cis)", "femail"]

    for (row, col) in mental_health_train.iterrows():

        if str.lower(col.Gender) in male_str:
            mental_health_train['Gender'].replace(to_replace=col.Gender, value='male', inplace=True)

        if str.lower(col.Gender) in female_str:
            mental_health_train['Gender'].replace(to_replace=col.Gender, value='female', inplace=True)

        if str.lower(col.Gender) in trans_str:
            mental_health_train['Gender'].replace(to_replace=col.Gender, value='trans', inplace=True)

    #Get rid of bullshit
    stk_list = ['A little about you', 'p']
    mental_health_train = mental_health_train[~mental_health_train['Gender'].isin(stk_list)]


    mental_health_train



    labelDict = {}
    for feature in mental_health_train:
        le = preprocessing.LabelEncoder()
        le.fit(mental_health_train[feature])
        le_name_mapping = dict(zip(le.classes_, le.transform(le.classes_)))
        mental_health_train[feature] = le.transform(mental_health_train[feature])
        # Get labels
        labelKey = 'label_' + feature
        labelValue = [*le_name_mapping]
        labelDict[labelKey] =labelValue


    mental_health_train


    mental_health_train.family_history.unique()

    x_train = mental_health_train.iloc[:,0:12]
    y_train = mental_health_train.iloc[:,12:13]

    from sklearn.linear_model import LogisticRegression

    algo = LogisticRegression();
    algo.fit(x_train,y_train)

    yp = algo.predict(a.reshape(1,-1))
    return yp

#FAA831
