# Scikit-Learn

## 1. Imports

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_absolute_error, accuracy_score
```

## 2. X and y

- `X` = input columns
- `y` = column to predict

```python
X = df[["Hours", "Previous_Marks"]]
y = df["Current_Marks"]
```

## 3. Split data

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=10
)
```

- Train data is used to teach the model.
- Test data is used to check predictions.
- `test_size=0.2` means 20% data for testing.

## 4. Models

**Linear Regression** — for predicting numbers, like marks.

```python
model = LinearRegression()
model.fit(X_train, y_train)
```

**Logistic Regression** — for predicting categories, like churn or no churn.

```python
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
```

## 5. Prediction

```python
predictions = model.predict(X_test)
```

For new data, give the same input columns used during training.

## 6. Check performance

**MAE** — for regression; shows average prediction error. Lower is better.

```python
mean_absolute_error(y_test, predictions)
```

**Accuracy** — for classification; shows how many predictions were correct.

```python
accuracy_score(y_test, predictions)
```

## IMP

- `fit()` trains the model.
- `predict()` makes predictions.
- Regression → numerical output.
- Classification → category output.
- Small datasets may not give reliable results.
