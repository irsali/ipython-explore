# %%
import pandas as pd
import numpy
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

iowa_file_path = './DataSets/home-data-for-ml-course_train.csv'

# %%
home_data = pd.read_csv(iowa_file_path)

# %%
home_data.describe()

# %%
home_data.columns


# %%
# home_data = home_data.dropna(axis=0)
# home_data.columns

# %%
# home_data.Price
y = home_data.SalePrice
feature_names = ['LotArea',
                 'YearBuilt',
                 '1stFlrSF',
                 '2ndFlrSF',
                 'FullBath',
                 'BedroomAbvGr',
                 'TotRmsAbvGrd'
                 ]

# %%
X = home_data[feature_names]

# %%
X.describe()

#%%
X.head()

#%%
iowa_model = DecisionTreeRegressor(random_state=1)

#%%
iowa_model.fit(X, y)

#%%
salePrices = iowa_model.predict(X)

#%%
dictionary = dict(zip(y, salePrices.tolist()))

#%%
print( {k:v for (k,v) in dictionary.items() if abs(k - v) > 0}) 

#%%
mean_absolute_error(y, salePrices)

#%%
# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

#%%
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

#%%
# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

#%%
