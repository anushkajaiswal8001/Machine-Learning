# Pandas — Project Quick Reference

## 1. Introduction

**Use:** Read, manipulate, clean, and analyze tabular data.

```python
import pandas as pd
```

## 2. Series

**Use:** Work with a single column of data.

```python
marks = pd.Series([50, 70, 85, 35])

marks.iloc[0]  # Access first value by position
marks.mean()   # Average
marks.max()    # Highest value
marks.min()    # Lowest value
```

## 3. DataFrame

**Use:** Store and work with data in rows and columns.

```python
data = {
    "Study_Hours": [2, 4, 5, 1],
    "Marks": [50, 70, 85, 35]
}

df = pd.DataFrame(data)
```

## 4. Importing and Inspecting Data

**Use:** Load a dataset and understand its structure.

```python
df = pd.read_csv("data.csv")

df.head()       # First 5 rows
df.shape        # Number of rows and columns
df.columns      # Column names
df.info()       # Data types and non-null counts
df.describe()   # Numerical summary
df.dtypes       # Data types of columns
```

## 5. Selection and Filtering

**Use:** Select specific columns or rows that match conditions.

```python
df["Marks"]                         # Single column
df[["Study_Hours", "Marks"]]        # Multiple columns
df.loc[0]                           # Row by label
df.iloc[0]                          # First row by position
df.iloc[0:3]                        # First 3 rows

df[df["Marks"] >= 40]               # Marks >= 40
df[df["Study_Hours"] > 3]           # Study hours > 3
df[(df["Marks"] >= 40) & (df["Study_Hours"] > 2)]
```

Use `&` for AND and `|` for OR. Put each condition in parentheses.

## 6. Aggregation and Counting

**Use:** Calculate statistics and count category values.

```python
df["Marks"].mean()        # Average
df["Marks"].max()         # Highest value
df["Marks"].min()         # Lowest value
df["Marks"].sum()         # Total
df["Marks"].count()       # Non-missing values

df.groupby("Class")["Marks"].mean()  # Average per class

df["Churn"].value_counts()  # Count Yes and No values
```

Use `groupby()` to summarize data for each category and `value_counts()` to count occurrences of each value.

## 7. Data Cleaning

**Use:** Find and handle missing values, duplicates, and incorrect data types.

```python
df.isnull().sum()                  # Missing values per column
df.dropna()                        # Remove rows with missing values
df.dropna(subset=["TotalCharges"]) # Remove rows missing this value
df["Marks"] = df["Marks"].fillna(0) # Fill missing marks with 0 if appropriate

df.duplicated().sum()              # Count duplicate rows
df = df.drop_duplicates()          # Remove duplicate rows
```

Convert text values into numbers:

```python
# Invalid values become NaN instead of causing an error
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)
```

**Note:** Don't replace missing values with `0` automatically. Choose a suitable method for the data.

## 8. Dummy Variables

**Use:** Convert categorical text columns into numerical columns for ML models.

```python
df = pd.get_dummies(
    df,
    columns=["Contract"],
    dtype=int
)
```

For example, `Contract` creates columns such as `Contract_Month-to-month` and `Contract_One year`.

- `1` = category matches the row.
- `0` = category does not match the row.

**Important:** New prediction data must have the same feature columns as the training data.

## 9. Selecting ML Features

**Use:** Separate input features (`X`) from the target (`y`).

```python
# Customer details used as model inputs
X = df[["tenure", "MonthlyCharges", "TotalCharges"]]

# Value the model must predict
y = df["Churn"]
```

- `X` = inputs.
- `y` = target to predict.

## Quick Reminders

- `head()` → preview data.
- `info()` → check data types and missing values.
- `value_counts()` → count categories.
- `isnull().sum()` → count missing values.
- `dropna()` → remove rows with missing values.
- `pd.to_numeric()` → convert values to numbers.
- `get_dummies()` → convert categories into numerical columns.
