import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.preprocessing import StandardScaler  
from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
# from sklearn.model_selection import cross_val_score
# from sklearn.pipeline import make_pipeline

df = pd.read_csv("data.csv")
print(df.head())
print(df.shape)
df.info()

print(df["Churn"].value_counts())  ## tellschow many customers leave service
# Check and convert TotalCharges to numeric
print(df["TotalCharges"].dtype)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna(subset = ["TotalCharges"]) # Remove rows with missing TotalCharges

## Convert categorical columns into dummy columns
df = pd.get_dummies(df,columns = ["Contract"])
df = pd.get_dummies(df,columns = ["InternetService"])
df = pd.get_dummies(df,columns = ["TechSupport"])
df = pd.get_dummies(df,columns = ["OnlineSecurity"])
df = pd.get_dummies(df,columns = ["PaperlessBilling"])


# Check missing values

print(df.isnull().sum())  ## tells that how many missing values are there in each column

# Select features (X) and target (Y)
X = df[["tenure","MonthlyCharges","TotalCharges","Contract_Month-to-month","Contract_One year","Contract_Two year","InternetService_DSL","InternetService_Fiber optic","InternetService_No","TechSupport_No","TechSupport_No internet service","TechSupport_Yes","OnlineSecurity_No","OnlineSecurity_No internet service","OnlineSecurity_Yes","PaperlessBilling_No","PaperlessBilling_Yes","SeniorCitizen"]]
Y = df["Churn"]
## split the data
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 10)


##scaling the features to bring them to a comparable scale
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ##train the model
# churn_model = make_pipeline(
#     StandardScaler(),
#     LogisticRegression(max_iter=1000, class_weight= "balanced")
# )
# churn_model.fit(X_train,Y_train)
# cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=10)

# scores = cross_val_score(churn_model, X, Y, cv=5, scoring="accuracy")
# print(scores)
# print(scores.mean())
# print(scores.std())
churn_model = LogisticRegression(max_iter=1000, class_weight= "balanced")

churn_model.fit(X_train,Y_train)

# Predict using the model's default threshold

predictions = churn_model.predict(X_test)
print("the prediction is ",predictions)

# Get probabilities for each class

probabilities = churn_model.predict_proba(X_test)
print(probabilities[:5])

yes_probabilities = probabilities[:, 1]

print(yes_probabilities[:5])

predictions_03 = []

# Apply a 30% decision threshold

for prob in yes_probabilities:
    if prob >= 0.3:
        predictions_03.append("Yes")
    else:
        predictions_03.append("No")
        
print(predictions_03[:10])

# Evaluate the model using the 30% threshold

print("Confusion Matrix:")
print(confusion_matrix(Y_test, predictions_03, labels=["No", "Yes"]))

print("Accuracy:")
print(accuracy_score(Y_test, predictions_03))

print("Recall:")
print(recall_score(Y_test, predictions_03, pos_label="Yes"))

print("F1-score:")
print(f1_score(Y_test, predictions_03, pos_label="Yes"))

#print(classification_report(Y_test, predictions_03))

## checking performance

##accuracy = accuracy_score(Y_test,predictions)
##print("accuracy is ",accuracy)
# recall = recall_score(Y_test,predictions,pos_label = "Yes")
# print(recall)

# result  = confusion_matrix(Y_test,predictions)
# print(result)

# f1 = f1_score(Y_test, predictions, pos_label="Yes")
# print("F1-score is", f1)
print("Default threshold results:")
print(confusion_matrix(Y_test, predictions))
print("Accuracy:", accuracy_score(Y_test, predictions))
print("Recall:", recall_score(Y_test, predictions, pos_label="Yes"))

print("30% threshold results:")
print(confusion_matrix(Y_test, predictions_03))
print("Accuracy:", accuracy_score(Y_test, predictions_03))
print("Recall:", recall_score(Y_test, predictions_03, pos_label="Yes"))
print(classification_report(Y_test, predictions_03))


# Take input from the user
tenure = float(input("Enter customer tenure (months): "))
monthly_charges = float(input("Enter monthly charges: "))
total_charges = float(input("Enter total charges: "))

contract = input("Enter contract (Month-to-month / One year / Two year): ").strip().lower()
internet = input("Enter internet service (DSL / Fiber optic / No): ")
tech_support = input("Has tech support? (Yes / No): ")
online_security = input("Has online security? (Yes / No): ")
paperless_billing = input("Paperless billing? (Yes / No): ")
senior_citizen = int(input("Is senior citizen? (1 = Yes, 0 = No): "))

# Create customer data in the same format as training data
new_customer = pd.DataFrame([{
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,

    "Contract_Month-to-month": int(contract == "month-to-month"),
"Contract_One year": int(contract == "one year"),
"Contract_Two year": int(contract == "two year"),

    "InternetService_DSL": int(internet == "DSL"),
    "InternetService_Fiber optic": int(internet == "Fiber optic"),
    "InternetService_No": int(internet == "No"),

    "TechSupport_No": int(tech_support == "No"),
    "TechSupport_No internet service": int(internet == "No"),
    "TechSupport_Yes": int(tech_support == "Yes"),

    "OnlineSecurity_No": int(online_security == "No"),
    "OnlineSecurity_No internet service": int(internet == "No"),    "OnlineSecurity_Yes": int(online_security == "Yes"),

    "PaperlessBilling_No": int(paperless_billing == "No"),
    "PaperlessBilling_Yes": int(paperless_billing == "Yes"),

    "SeniorCitizen": senior_citizen
}])

# Scale the new customer data
new_customer_scaled = scaler.transform(new_customer)

# Predict churn probability
probability = churn_model.predict_proba(new_customer_scaled)[0][1]

# Apply 30% threshold
if probability >= 0.30:
    print("Prediction: Customer may churn")
else:
    print("Prediction: Customer is less likely to churn")

print("Churn probability:", round(probability * 100, 2), "%")