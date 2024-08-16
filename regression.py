import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
print (data)

def loss_funct(m, b, points):
    error_aggr = 0
    for i in range(len(points)):
        x = points.iloc[i].uv_radiation_level
        y = points.iloc[i].cancer_incidence_p100
        error_aggr += (y - (m*x+b))**2
    error_aggr / float(len(points))

def grad_descent(m_now, b_now, points, L): 
    m_gradient = 0
    b_gradient = 0