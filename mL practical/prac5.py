'''
Predict the price of the Uber ride from a given pickup point to the agreed drop-off location.
Perform following tasks:
1. Pre-process the dataset.
2. Identify outliers.
3. Check the correlation.
4. Implement linear regression and random forest regression models.
5. Evaluate the models and compare their respective scores like R2, RMSE, etc.

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

df = pd.read_csv('uber.csv')
df.info()

#################### 1. Pre-process the dataset      ############################################################

df.shape

df.head()

df.isnull()

df.drop(columns=["Unnamed: 0", "key"], inplace=True)
df.head()

df.isnull().sum()

df['dropoff_latitude'].fillna(df['dropoff_latitude'].mean(),inplace = True)
df['dropoff_longitude'].fillna(value=df['dropoff_longitude'].median(),inplace = True)

df.dtypes

# From the above output, we see that the data type of 'pickup_datetime' is 'object
# But 'pickup_datetime'is a date time stamp variable, which is wrongly interpreted as 'object', so we will convert this variable data type to 'datetime'.
df.pickup_datetime = pd.to_datetime(df.pickup_datetime)
df.dtypes

# we will extract time feature from the 'pickup_datetime' 
# we will add a variable which measures the distance between pickup and drop
df = df.assign(hour = df.pickup_datetime.dt.hour,
               day = df.pickup_datetime.dt.day,
               month = df.pickup_datetime.dt.month,
               year = df.pickup_datetime.dt.year,
               dayofweek = df.pickup_datetime.dt.dayofweek)

df

df = df.drop(["pickup_datetime"], axis =1)
df

# function to calculate the travel distance from the longitudes and latitudes
from math import *

def distance_formula(longitude1, latitude1, longitude2, latitude2):
    travel_dist = []
    
    for pos in range (len(longitude1)):
        lon1, lan1, lon2, lan2 = map(radians, [longitude1[pos], latitude1[pos], longitude2[pos], latitude2[pos]])
        dist_lon = lon2 - lon1
        dist_lan = lan2 - lan1
        
        a = sin(dist_lan/2)**2 + cos(lan1) * cos(lan2) * sin(dist_lon/2)**2
        
        #radius of earth = 6371
        c = 2 * asin(sqrt(a)) * 6371 
        travel_dist.append(c)
        
    return  travel_dist

df['dist_travel_km'] = distance_formula(df.pickup_longitude.to_numpy(), df.pickup_latitude.to_numpy(), df.dropoff_longitude.to_numpy(), df.dropoff_latitude.to_numpy())

#######################################################################################################################################################################################################

####################        2. Identify outliers   ########################################################################


df.plot(kind = "box",subplots = True,layout = (6,2),figsize=(15,20)) #Boxplot to check the outliers
plt.show()


#Using the InterQuartile Range to fill the values
def remove_outlier(df1 , col):
    Q1 = df1[col].quantile(0.25)
    Q3 = df1[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_whisker = Q1-1.5*IQR
    upper_whisker = Q3+1.5*IQR
    df[col] = np.clip(df1[col] , lower_whisker , upper_whisker)
    return df1

def treat_outliers_all(df1 , col_list):
    for c in col_list:
        df1 = remove_outlier(df , c)
    return df1

df = treat_outliers_all(df , df.iloc[: , 0::])


#Boxplot shows that dataset is free from outliers
df.plot(kind = "box",subplots = True,layout = (7,2),figsize=(15,20)) 
plt.show()


##############################################################################################################################

#########################  3. Check the correlation.           ##################################################

#Function to find the correlation
corr = df.corr() 
corr

print(corr.style.background_gradient(cmap='BuGn'))

fig,axis = plt.subplots(figsize = (10,6))
sns.heatmap(df.corr(),annot = True) #Correlation Heatmap (Light values means highly correlated)


###################################################################################################################################################################

#4. Implement linear regression and random forest regression models.

# Dividing the dataset into feature and target values 
df_x = df[['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','hour','day','month','year','dayofweek','dist_travel_km']]
df_y = df['fare_amount']

df_x = df[['pickup_longitude','pickup_latitude','dropoff_longitude','dropoff_latitude','passenger_count','hour','day','month','year','dayofweek','dist_travel_km']].values.reshape(-1, 1) #Independent Variable
df_y  = df['fare_amount'].values.reshape(-1, 1) #Dependent Variable

#Standardization
from sklearn.preprocessing import StandardScaler
std = StandardScaler()
df_x = std.fit_transform(df_x)
print(df_x)
df_y = std.fit_transform(df_y)
print(df_y)

# Dividing the dataset into training and testing dataset
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=1)
df

df.dtypes


from sklearn.linear_model import LinearRegression
from sklearn import metrics

# initialize the linear regression model
l_reg = LinearRegression()
l_reg.fit(x_train, y_train)
print("Training set score: {:.2f}".format(l_reg.score(x_train, y_train)))
print("Test set score: {:.7f}".format(l_reg.score(x_test, y_test)))

y_pred = l_reg.predict(x_test)
result = pd.DataFrame()
result['Actual'] = y_test
result['Predicted'] = y_pred
result.sample(10)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Absolute % Error:', metrics.mean_absolute_percentage_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print('R Squared (R²):', np.sqrt(metrics.r2_score(y_test, y_pred)))

'''Visualization
Model RMSE R-Squared
0 Linear Regresion model 0.52012 0.856765
RandomForestRegressor
Training the RandomForestRegressor model on the training set
'''
# error - x and y must be the same size
plt.subplot(2, 2, 1)
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, l_reg.predict(x_train), color ="blue")
plt.title("Fare vs Distance (Training Set)")
plt.ylabel("fare_amount")
plt.xlabel("Distance")


plt.subplot(2, 2, 2)
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, l_reg.predict(x_train), color ="blue")
plt.ylabel("fare_amount")
plt.xlabel("Distance")
plt.title("Fare vs Distance (Test Set)")

plt.tight_layout()
plt.show()


from sklearn.ensemble import RandomForestRegressor

#Here n_estimators means number of trees you want to build before making the prediction
rf = RandomForestRegressor(n_estimators=100)
rf.fit(x_train,y_train)

y_pred_RF = rf.predict(x_test)
result = pd.DataFrame()
result['Actual'] = y_test
result['Predicted'] = y_pred_RF
result.sample(10)

########################################################################################################################################

#5. Evaluate the models and compare their respective scores like R2, RMSE, etc

cols = ['Model', 'RMSE', 'R-Squared']

# create a empty dataframe of the colums
# columns: specifies the columns to be selected
result_tabulation = pd.DataFrame(columns = cols)

from sklearn import metrics 
from sklearn.metrics import r2_score 

reg_RMSE = np.sqrt(metrics.mean_squared_error(y_test, y_pred_lin))
reg_squared = r2_score(y_test, y_pred_lin)

full_metrics = pd.Series({'Model': "Linear Regression", 'RMSE' : reg_RMSE, 'R-Squared' : reg_squared})

# append our result table using append()
# ignore_index=True: does not use the index labels
# python can only append a Series if ignore_index=True or if the Series has a name
result_tabulation = result_tabulation.append(full_metrics, ignore_index = True)

# print the result table
result_tabulation

rf_RMSE = np.sqrt(metrics.mean_squared_error(y_test, y_pred_rf))
rf_squared = r2_score(y_test, y_pred_rf)


full_metrics = pd.Series({'Model': "Random Forest ", 'RMSE':rf_RMSE, 'R-Squared': rf_squared})
# append our result table using append()
# ignore_index=True: does not use the index labels
# python can only append a Series if ignore_index=True or if the Series has a name
result_tabulation = result_tabulation.append(full_metrics, ignore_index = True)

# print the result table
result_tabulation




