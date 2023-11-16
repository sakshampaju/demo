"""Classify the email using the binary classification method. Email Spam detection has two
states: a) Normal State – Not Spam, b) Abnormal State – Spam. Use K-Nearest Neighbors and
Support Vector Machine for classification. Analyze their performance. """

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
 
#load the datatset
df = pd.read_csv("emails.csv")
df.head()
  
df.shape

df.columns

df.isnull().sum()

# Selecting Columns for training 
df.drop(['Email No.'],axis=1,inplace=True)
X = df.drop(['Prediction'],axis = 1)
y = df['Prediction']

from sklearn.preprocessing import scale
X = scale(X)


# split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

X_train.shape

##################################### KNN ##########################################################

#import KNN classifier from sklearn. neighbors

from sklearn.neighbors import KNeighborsClassifier

#KNN with k = 5
model_knn = KNeighborsClassifier(n_neighbors=5)
 
#Train the Model using fit Function
model_knn.fit(X_train, y_train)

#Predict the Trained Model
y_pred = model_knn.predict(X_test)

#Print the Predicted Values
print("Prediction",y_pred)

#Display the Accuracy of the Model (Testing)
from sklearn import metrics
print("KNN accuracy = ",metrics.accuracy_score(y_test,y_pred))

#Model Evaluation: R2, MAE, MSE and RMSE
meanAbErr = metrics.mean_absolute_error(y_test, y_pred)
meanSqErr = metrics.mean_squared_error(y_test, y_pred)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print('R squared: {:.2f}'.format(model_knn.score(X,y)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)

##################################### SVC ##########################################################

#import SVM classifier (SVC) from sklearn.svm
from sklearn.svm import SVC

# cost C = 1
model_svc = SVC(C = 1)

#Train the Model using fit Function
model_svc.fit(X_train, y_train)

#Predict the Trained Model
y_pred_svc = model_svc.predict(X_test)

#Print the Predicted Values
print("Prediction",y_pred_svc)

#Display the Accuracy of the Model (Testing)
print("SVM accuracy = ",metrics.accuracy_score(y_test,y_pred_svc))


#Model Evaluation: R2, MAE, MSE and RMSE
meanAbErr = metrics.mean_absolute_error(y_test, y_pred_svc)
meanSqErr = metrics.mean_squared_error(y_test, y_pred_svc)
rootMeanSqErr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_svc))
print('R squared: {:.2f}'.format(model_svc.score(X,y)*100))
print('Mean Absolute Error:', meanAbErr)
print('Mean Square Error:', meanSqErr)
print('Root Mean Square Error:', rootMeanSqErr)

