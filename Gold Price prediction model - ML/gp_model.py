# to create polynomial regression model for gold prices

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("gp_march24.csv")
print(data)

feature = data[["Year"]]
target = data["Price"]

pf = PolynomialFeatures(degree = 7)
pfeature = pf.fit_transform(feature)

model = LinearRegression()
model.fit(pfeature, target)

y = float(input("enter the year : "))
py = pf.transform([[y]])
p = model.predict(py)
print("price : ",round(p[0],2))


