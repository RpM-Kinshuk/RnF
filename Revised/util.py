import numpy as np
import pandas as pd

def data_load():
    data = np.loadtxt('Rnf.txt', delimiter=',')
    x = data[:,1:6]
    y = data[:,6]
    #y = (np.rint(y)).astype(int)
    return x, y

def load_data():
    data = pd.read_csv('Rainfall_data.csv')
    x = data.drop(['Year', 'Precipitation'], axis=1)
    y = data['Precipitation']
    m = data['Month']
    tmp = data['Temperature']
    humidity = data['Relative Humidity']
    yr = data['Year']
    return x, y, m, tmp, humidity, yr

def givepw():
    return "R@r58r#$"