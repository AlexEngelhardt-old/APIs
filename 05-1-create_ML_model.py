from sklearn import linear_model
import pickle
import numpy as np

N = 100
x1 = np.random.rand(N) * 100
x2 = np.random.rand(N) * 100
epsilon = np.random.randn(N) * 2
y = 3 * x1 - 4 * x2 + 2 + epsilon

X = np.array([x1, x2]).T

lm = linear_model.LinearRegression()
lm.fit(X, y)

pickle.dump(lm, open('05_model.pkl', 'wb'))
