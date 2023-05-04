import numpy as np 
from sklearn.linear_model import LinearRegression

x = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

model = LinearRegression()

model.fit(x,y)

r_sq = model.score(x,y)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

y_pred = model.predict(x)
print(f"predicted reponse: \n {y_pred}")


x = [
    [0,1],[5,1],[15,2],[25,5],[35,11],[45,15],[55,34],[60,35]
]

y= [4,5,20,14,32,22,38,43]

x,y = np.array(x), np.array(y)

model = LinearRegression()
model.fit(X= x,y=y)

r_sq = model.score(x,y)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

y_pred = model.predict(x)
print(f"predicted reponse: \n {y_pred}")

x_new = np.arange(10).reshape((-1,2))

y_new= model.predict(x_new)
print(y_new)