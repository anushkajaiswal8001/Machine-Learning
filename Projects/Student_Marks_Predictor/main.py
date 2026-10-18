import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print(df)

print(df.head(4))
print(df.shape)
df.info()

plt.scatter(df["Hours"],df["Marks"])

plt.title("Marks Predictor")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()