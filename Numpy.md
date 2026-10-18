# INTRODUCTION

NumPy stands for Numerical Python. It is a Python library used for numerical calculations and working with arrays.

## Importing NumPy

```python
import numpy as np
```

`np` is the short name used for NumPy.


##  Creating Arrays

**Use:** Store numerical data for calculations.

```python
import numpy as np

study_hours = np.array([1, 2, 3, 4, 5])
marks = np.array([35, 40, 50, 65, 80])
```

## Array Properties

**Use:** Check the size and dimensions of data.

```python
marks.shape
marks.ndim
marks.size
```

##  Indexing and Slicing

**Use:** Select specific values or parts of an array.

```python
marks[0]       # First value
marks[1:4]     # Values at indices 1, 2, 3
marks[::2]     # Every second value
```

##  Array Operations

**Use:** Perform calculations on every element.

```python
marks + 5
marks * 2
marks / 10
```

## Statistical Functions

**Use:** Analyze numerical data.

```python
np.mean(marks)  # Average
np.max(marks)   # Highest value
np.min(marks)   # Lowest value
np.sum(marks)   # Total
np.std(marks)   # Standard deviation
```

##  Aggregation with axis

**Use:** Calculate statistics row-wise or column-wise.

```python
marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 90, 88]
])

np.mean(marks, axis=1)  # Average for each student
np.mean(marks, axis=0)  # Average for each subject
```

##  Filtering

**Use:** Select values that satisfy a condition.

```python
marks[marks >= 40]
marks[marks < 40]
marks[(marks >= 40) & (marks < 70)]
```

##  Conditional Values with np.where()

**Use:** Assign labels based on a condition.

```python
result = np.where(marks >= 40, "Pass", "Fail")
```

##  Broadcasting

**Use:** Perform operations between compatible array shapes.

```python
marks = np.array([40, 50, 60])
adjusted_marks = marks + 5
```

NumPy compares shapes from right to left. Dimensions must match or one of them must be `1`.

##  Random Data

**Use:** Generate sample data for testing and practice.

```python
rng = np.random.default_rng(42)

numbers = rng.integers(1, 10, size=5)
decimals = rng.uniform(0, 1, size=5)
```

## Shuffle and Choice

**Use:** Randomly rearrange data or select random samples.

```python
rng.shuffle(marks)  # Modifies the original array

sample = rng.choice(marks, size=2, replace=False)
```

`replace=False` prevents selecting the same element more than once.

