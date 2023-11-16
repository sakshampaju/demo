"""
Implement K-Means clustering/ hierarchical clustering on sales_data_sample.csv dataset.
Determine the number of clusters using the elbow method.

"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('Ignore')
import matplotlib.pyplot as plt

df=pd.read_csv("sales_data_sample.csv",encoding='latin 1')

df.head()

df.columns

print(df.isnull().sum())

df.info()

df.describe()

df.shape

#convert categorical data into int
'''
QUANTITYORDERED ,PRICEEACH ,ORDERLINENUMBER  ,SALES, /ORDERDATE, QTR_ID, MONTH_ID ,
 YEAR_ID ,  PRODUCTLINE , MSRP , PRODUCTCODE , DEALSIZE /COUNTRY  

'''
x=df

x_drop=['CUSTOMERNAME','ADDRESSLINE1','ADDRESSLINE2','CITY','COUNTRY','TERRITORY','CONTACTLASTNAME','CONTACTFIRSTNAME']

# Check if the columns exist
print('PHONE' in x.columns)
print('STATE' in x.columns)
print('POSTALCODE' in x.columns)

x= x.drop(x_drop,axis=1)

print(x.isnull().sum())

x.drop('PHONE',axis=1,inplace=True)
x.drop('STATE',axis=1,inplace=True)
x.drop('POSTALCODE',axis=1,inplace=True)

print(x.dtypes)

x.drop('ORDERDATE',axis=1,inplace=True)
x.drop('STATUS',axis=1,inplace=True)

#Converting the categorical columns.  
productline = pd.get_dummies(df['PRODUCTLINE'])
Dealsize = pd.get_dummies(df['DEALSIZE']) 

x = pd.concat([x,productline,Dealsize], axis = 1)

print(x.dtypes)

x.drop('PRODUCTLINE',axis=1,inplace=True)
x.drop('DEALSIZE',axis=1,inplace=True)

 #Converting the datatype
x['PRODUCTCODE'] = pd.Categorical(x['PRODUCTCODE']).codes

x.drop('ORDERDATE',axis=1,inplace=True)

####################################################################

from sklearn.preprocessing import MinMaxScaler

ms = MinMaxScaler()

x = ms.fit_transform(x)


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=4, random_state=42) 

kmeans.fit(x)

y_kmeans = kmeans.fit_predict(x)
y_kmeans

kmeans.cluster_centers_

kmeans.inertia_

df['Cluster'] = kmeans.labels_

# Visualize clusters
plt.scatter(x[:, 0], x[:, 1], c=df['Cluster'], cmap='viridis', edgecolor='k', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', marker='X', label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()


cs = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 42)
    kmeans.fit(x)
    cs.append(kmeans.inertia_)
    
plt.plot(range(1, 11), cs)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('CS')
plt.show()
