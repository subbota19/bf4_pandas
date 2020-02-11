from sklearn import neighbors, linear_model
from graphic import census_2011, census_2015, land_area
import numpy as np

model_1 = linear_model.LinearRegression()

model_2 = neighbors.KNeighborsRegressor(n_neighbors=2)

# model learning this model_1 is learning use all data and second model use k-element neighbors that allows for us
# get more accuracy data
model_1.fit(np.c_[census_2011], np.c_[land_area])

model_2.fit(np.c_[census_2011], np.c_[land_area])

# in the end we can predict areas any regions(use their properties)
print(model_1.predict([[100_000]]))
print(model_2.predict([[100_000]]))
