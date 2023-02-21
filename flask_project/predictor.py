from util import *
import numpy as np
from sklearn.ensemble import RandomForestRegressor
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import SGDRegressor
# from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def train_on_data():
    x_train, y_train, month, temp, humidity, year = load_data()
    #x_train, y_train = data_load()
    rf_model = RandomForestRegressor()
    rf_model.fit(x_train.values,y_train)
    return rf_model

# print(y_train)
# print(x_train)
# scl = StandardScaler()
# x_n = scl.fit_transform(x_train)
# sgr = LinearRegression()
# sgr = SGDRegressor(max_iter=1000000)
# sgr.fit(x_train,y_train)

# b_n = sgr.intercept_
# w_n = sgr.coef_

def predict_rainfall(a,b,c,d,e):
    rf_model = train_on_data()
    inp = np.array([a,b,c,d,e])
    inp = inp.reshape(1,-1)
    return rf_model.predict(inp)[0]

# inp_tst = np.array([6,1,20.08,82.31,12.02])
# inp_tst = inp_tst.reshape(1,-1)

# print('\n\n\n\nRainfall = ',rf_model.predict(inp_tst)[0])
# print('\n\n\n\n')