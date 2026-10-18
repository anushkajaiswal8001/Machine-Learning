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

marks.iloc[0]  # Access by position
marks.mean()   # Calculate average
marks.max()    # Highest value
marks.min()    # Lowest value
```

## 3. DataFrame

**Use:** Store and work with data arranged in rows and columns.

```python
data = {
    "Study_Hours": [2, 4, 5, 1],
    "Marks": [50, 70, 85, 35]
}

df = pd.DataFrame(data)
```

## 4. Importing Data

**Use:** Load datasets from files.

```python
df = pd.read_csv("students.csv")
df = pd.read_json("students.json")
```

Inspect the dataset:

```python
df.head()       # First 5 rows
df.shape        # Number of rows and columns
df.columns      # Column names
df.info()       # Data types and non-null counts
df.describe()   # Statistical summary
```

## 5. Selection

**Use:** Select specific columns or rows.

```python
df["Marks"]                         # Single column
df[["Study_Hours", "Marks"]]        # Multiple columns
df.loc[0]                           # Row by label
df.iloc[0]                          # First row by position
df.iloc[0:3]                        # First 3 rows
```

## 6. Filtering

**Use:** Select rows that satisfy conditions.

```python
df[df["Marks"] >= 40]

df[df["Study_Hours"] > 3]

df[(df["Marks"] >= 40) & (df["Study_Hours"] > 2)]
```

Use `&` for AND and `|` for OR. Put each condition in parentheses.

## 7. Aggregation

**Use:** Calculate statistics and summarize data.

```python
df["Marks"].mean()      # Average
df["Marks"].max()       # Highest value
df["Marks"].min()       # Lowest value
df["Marks"].sum()       # Total
df["Marks"].count()     # Number of non-missing values

df.groupby("Class")["Marks"].mean()
```

Use `groupby()` to calculate statistics for each category.

## 8. Data Cleaning

**Use:** Identify and handle missing or duplicate data.

```python
df.isnull().sum()        # Missing values per column
df.dropna()              # Remove rows containing missing values
df.fillna(0)             # Replace missing values with 0
df.duplicated().sum()    # Count duplicate rows
df.drop_duplicates()     # Remove duplicate rows
```

Check data types:

```python
df.dtypes
```

Convert a column when appropriate:

```python
df["Marks"] = pd.to_numeric(df["Marks"], errors="coerce")
```

`errors="coerce"` converts invalid values to `NaN`.

