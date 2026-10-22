# Scikit-Learn

## 1. Imports

```python
# Splits data into training and testing sets
# We use it to train the model on one part and evaluate it on unseen data
from sklearn.model_selection import train_test_split

# LinearRegression predicts numerical values, such as student marks
from sklearn.linear_model import LinearRegression

# LogisticRegression predicts categories, such as Churn = Yes or No
from sklearn.linear_model import LogisticRegression

# StandardScaler scales numerical features to comparable ranges
from sklearn.preprocessing import StandardScaler

# Measures average prediction error for regression
from sklearn.metrics import mean_absolute_error

# Measures the proportion of correct predictions
from sklearn.metrics import accuracy_score

# Measures how many actual positive cases were correctly identified
from sklearn.metrics import recall_score

# Balances precision and recall into one score
from sklearn.metrics import f1_score

# Shows correct and incorrect predictions for each class
from sklearn.metrics import confusion_matrix

# Shows precision, recall, F1-score, and support for each class
from sklearn.metrics import classification_report
```

## 2. X and y

```python
# X contains input features used by the model to make predictions
X = df[["Hours", "Previous_Marks"]]

# y contains the target value that the model must learn to predict
y = df["Current_Marks"]
```

For the Customer Churn project:

```python
# Customer details are the inputs used to predict churn
X = df[["tenure", "MonthlyCharges", "TotalCharges"]]

# Churn is the target because we want to predict whether a customer leaves
y = df["Churn"]
```

## 3. Split Data

```python
# Splits the dataset so we can train the model and evaluate it separately
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,     # Keeps 20% of the data for testing and 80% for training
    random_state=10    # Makes the random split reproducible
)
```

- `X_train`, `y_train`: used to teach the model.
- `X_test`, `y_test`: used to check how well the model predicts unseen data.
- `test_size=0.2`: keeps some data separate so evaluation is not done only on training examples.
- `random_state=10`: helps produce the same split when the code is run again on the same data.

## 4. Models

### Linear Regression

```python
# Creates a model for predicting numerical values, such as marks
model = LinearRegression()

# Trains the model using input features and their known target values
model.fit(X_train, y_train)
```

### Logistic Regression

```python
# Creates a classification model for predicting categories such as Yes or No
# max_iter=1000 allows more training iterations if the model needs them
model = LogisticRegression(max_iter=1000)

# Learns patterns between customer features and the Churn target
model.fit(X_train, y_train)
```

## 5. Prediction

```python
# Uses the trained model to predict the target for the test inputs
predictions = model.predict(X_test)
```

For a new customer:

```python
# The new customer's features must match the features used during training
# This lets the model make a prediction for a customer it has not seen before
new_prediction = model.predict(new_customer)
```

## 6. Feature Scaling

```python
# Creates a scaler that standardizes numerical features
scaler = StandardScaler()

# Learns the scaling values from training data and scales that data
# We fit only on training data to avoid leaking information from the test set
X_train = scaler.fit_transform(X_train)

# Applies the same training-data scaling values to the test data
# We do not fit again because test data must remain unseen during preprocessing
X_test = scaler.transform(X_test)
```

For new customer data:

```python
# Applies the same scaling learned from training data
# This keeps new customer features in the same format as model training data
new_customer_scaled = scaler.transform(new_customer)
```

**Important:** The new customer's feature columns and their order must match the training features.

## 7. Categorical Data: Dummy Variables

```python
# Converts text categories into numerical columns that a model can use
# dtype=int makes the new dummy columns contain 0 and 1 integers
df = pd.get_dummies(
    df,
    columns=["Contract"],
    dtype=int
)
```

For example, `Contract` can become:

- `Contract_Month-to-month`
- `Contract_One year`
- `Contract_Two year`

A value of `1` means the category matches that row; `0` means it does not.

```python
# Example: create a dummy feature for a month-to-month contract
df["Contract_Month-to-month"] = (
    df["Contract"] == "Month-to-month"
).astype(int)
```

**Why use dummy variables?** A model cannot directly use categories such as `"Month-to-month"` as ordinary numerical inputs. Dummy variables represent those categories using numbers.

**Important:** New customer data must use the same dummy columns as the training data.

## 8. Handling Missing and Non-Numeric Data

```python
# Converts TotalCharges from text into numeric values
# Invalid values become NaN instead of causing a conversion error
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

# Removes rows where TotalCharges is missing
# This avoids training on rows with no usable value for this feature
df = df.dropna(subset=["TotalCharges"])
```

**Why?** A column may look numeric but be stored as text. Converting it allows numerical calculations and model training. Missing values need to be handled before fitting many Scikit-Learn models.

## 9. Model Evaluation

### Mean Absolute Error (MAE)

```python
# Calculates the average absolute difference between actual and predicted values
# Used for regression; a lower MAE means predictions are closer on average
mae = mean_absolute_error(y_test, predictions)
```

### Accuracy

```python
# Calculates the proportion of all predictions that are correct
# Useful, but can be misleading when target classes are imbalanced
accuracy = accuracy_score(y_test, predictions)
```

### Recall

```python
# Measures how many actual positive cases the model successfully identifies
# In churn prediction, this tells us how many actual churners were caught
recall = recall_score(
    y_test,
    predictions,
    pos_label="Yes"
)
```

### F1-score

```python
# Combines precision and recall into one score
# Useful when we want to consider both missed positive cases and false alarms
f1 = f1_score(
    y_test,
    predictions,
    pos_label="Yes"
)
```

### Confusion Matrix

```python
# Shows counts of correct and incorrect predictions for each class
# Specifying label order makes it clear how to read the matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=["No", "Yes"]
)
```

With labels `["No", "Yes"]`, the matrix is arranged as:

```text
# [[True Negatives, False Positives],
#  [False Negatives, True Positives]]
```

- **True Negative (TN):** correctly predicted `No`.
- **False Positive (FP):** predicted `Yes`, but actual value was `No`.
- **False Negative (FN):** predicted `No`, but actual value was `Yes`.
- **True Positive (TP):** correctly predicted `Yes`.

### Classification Report

```python
# Displays precision, recall, F1-score, and the number of actual examples
# for each class, helping us compare performance for Yes and No separately
print(classification_report(y_test, predictions))
```

## 10. Predicting Probabilities

```python
# Returns the estimated probability of each class for every test example
# Useful when we want to choose a decision threshold ourselves
probabilities = model.predict_proba(X_test)

# Checks which class corresponds to each probability column
# We must check this before selecting a column
print(model.classes_)
```

If the class order is `["No", "Yes"]`:

```python
# Selects the probability column corresponding to Yes
yes_probabilities = probabilities[:, 1]
```

**Why use probabilities?** `predict()` gives the predicted class, while `predict_proba()` lets us see how strongly the model estimates each class and apply a custom threshold.

## 11. Decision Threshold

```python
# Creates an empty list to store predictions using a 30% threshold
predictions_03 = []

# Checks each customer's estimated probability of churn
for prob in yes_probabilities:

    # Predicts churn when the estimated probability is at least 30%
    if prob >= 0.30:
        predictions_03.append("Yes")

    # Otherwise, predicts that the customer will not churn
    else:
        predictions_03.append("No")
```

- A lower threshold usually identifies more positive cases and increases recall, but can create more false positives.
- A higher threshold usually predicts fewer positive cases, potentially missing more actual positive cases.
- Choose a threshold according to the project's goal.

**Important:** A 73% predicted probability is an estimate, not a guarantee that the customer will churn.

## 12. Class Imbalance

```python
# Counts how many examples belong to each target class
# Helps us check whether one class is much more common than another
print(df["Churn"].value_counts())
```

```python
# Gives greater weight to underrepresented classes during model training
# This can help the model pay more attention to the minority class
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)
```

**Why use it?** In the churn dataset, there are many more `No` examples than `Yes` examples. Balanced class weights help address this difference.

However, this may also increase false positives. Always evaluate the results to see whether it helps.

## Important Reminders

- `fit()` trains the model.
- `predict()` predicts numerical values or classes.
- `predict_proba()` returns estimated class probabilities when supported.
- Regression predicts numerical values; classification predicts categories.
- Split the data before fitting the scaler.
- Use the same preprocessing for training, testing, and new data.
- Accuracy alone may be misleading for imbalanced datasets.
- A good score does not guarantee correct predictions for every new example.
