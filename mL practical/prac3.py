'''Implement K-Nearest Neighbors algorithm on diabetes.csv dataset. Compute confusion
matrix, accuracy, error rate, precision and recall on the given dataset.'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import (confusion_matrix,accuracy_score,precision_score,recall_score )

df=pd.read_csv("diabetes.csv")

print(df)

df.columns

df.shape

df.head()

df.dtypes

print(df.isnull().sum)

diabetes_data_copy = df.copy(deep = True)
diabetes_data_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

## showing the count of Nans
print(diabetes_data_copy.isnull().sum())

p = df.hist(figsize = (20,20))

diabetes_data_copy['Glucose'].fillna(diabetes_data_copy['Glucose'].mean(), inplace = True)
diabetes_data_copy['BloodPressure'].fillna(diabetes_data_copy['BloodPressure'].mean(), inplace = True)
diabetes_data_copy['SkinThickness'].fillna(diabetes_data_copy['SkinThickness'].median(), inplace = True)
diabetes_data_copy['Insulin'].fillna(diabetes_data_copy['Insulin'].median(), inplace = True)
diabetes_data_copy['BMI'].fillna(diabetes_data_copy['BMI'].median(), inplace = True)

p = diabetes_data_copy.hist(figsize = (20,20))

p=sns.pairplot(diabetes_data_copy, hue = 'Outcome')

df.shape

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x =  pd.DataFrame(sc_X.fit_transform(diabetes_data_copy.drop(["Outcome"],axis = 1),),
        columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age'])

y=df['Outcome']


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)

print(x_train.shape)

from sklearn.neighbors import KNeighborsClassifier

model_knn=KNeighborsClassifier(n_neighbors=4)

model_knn.fit(x_train,y_train)

y_pred=model_knn.predict(x_test)

conf_mat=confusion_matrix(y_test,y_pred)

print(conf_mat)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

Accuracy=accuracy_score(y_test,y_pred)
print("Accuracy : ",Accuracy)
print("Precision : ",precision_score(y_test,y_pred))
print("Recall : ",recall_score(y_test,y_pred))
print("error rate : ",1-Accuracy)



