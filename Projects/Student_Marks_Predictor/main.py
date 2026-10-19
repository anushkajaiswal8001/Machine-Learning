import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("data.csv",index_col = None)
df.index = [f"Student{i}" for i in range(1,len(df)+1)]
X = df[["Hours","Previous_Marks"]]

Y = df["Current_Marks"]

## split the data 

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state = 10) 

## create the model

marks_model = LinearRegression()

## training the model

marks_model.fit(X_train,Y_train)

 ## checking Model performance

test_predictions = marks_model.predict(X_test)
print("Predicted test Marks:",test_predictions)

print("Actual Marks:", Y_test.values)

error = mean_absolute_error(Y_test,test_predictions)
print("Mean Absolute Error: ",error)


## user input for new data
Hours = float(input("Enter study hours: "))
Previous_Marks = float(input("Enter previous marks: "))
new_student = pd.DataFrame({
            "Hours": [Hours],
            "Previous_Marks": [Previous_Marks]
})

## predicting

predictions = marks_model.predict(new_student)
print("Predicted Marks:",predictions[0])

print(df)

print(df.head(4))
print(df.shape)
df.info()

plt.scatter(df["Hours"],df["Current_Marks"])

plt.title("Marks Predictor")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

