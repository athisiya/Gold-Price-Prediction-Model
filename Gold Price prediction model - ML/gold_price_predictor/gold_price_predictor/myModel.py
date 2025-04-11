import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_csv("gold_price_predictor/gp_march24.csv")

feature = data[["Year"]]
target = data["Price"]

pf = PolynomialFeatures(degree=7)
pfeature = pf.fit_transform(feature)

model = LinearRegression()
model.fit(pfeature, target)

def predict_price(year):
    py = pf.transform([[year]])
    price = model.predict(py)
    return round(price[0], 2)
