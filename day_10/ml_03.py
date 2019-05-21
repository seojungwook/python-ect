# -*- coding: utf-8 -*-

import numpy as np

from sklearn.linear_model import LinearRegression

x_data = np.array([[10], [20], [30], [40], [50]]).reshape(-1, 1)
y_data = np.array([95, 203, 293, 397, 503])

model = LinearRegression()
model.fit(x_data, y_data)
print(model.predict(np.array([10]).reshape(-1, 1))[0])