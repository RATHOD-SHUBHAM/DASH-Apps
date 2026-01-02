from sklearn.datasets import fetch_california_housing

df = fetch_california_housing(as_frame = True).frame

df.to_csv('housing.csv', index = None)