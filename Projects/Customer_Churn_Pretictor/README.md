# Customer Churn Prediction

## About the Project

This is a beginner Machine Learning project built using Python to predict whether a telecom customer is likely to leave the service (churn) or continue using it.

The project uses customer information such as tenure, monthly charges, total charges, contract type, internet service, and other service details to make predictions.

## Dataset

- Dataset: Telco Customer Churn
- Total records: 7,043
- Total columns: 21
- Target column: `Churn`
- Target values: `Yes` and `No`

## Technologies Used

- Python
- Pandas
- Scikit-learn

## Machine Learning Model

**Logistic Regression** is used to predict customer churn.

The dataset is split into training and testing sets using `train_test_split`. `StandardScaler` is used to scale the features before training the model.

## Model Evaluation

The model was evaluated using a confusion matrix, accuracy, recall, and F1-score.

### Default Threshold (50%)

- Accuracy: 72.92%
- Recall: 82.55%

### Custom Threshold (30%)

- Accuracy: 62.12%
- Recall: 93.63%
- F1-score: 55.91%

The 30% threshold identifies more customers who may churn, but it also produces more false-positive predictions. The choice of threshold depends on the business goal.

## New Customer Prediction

The project also accepts details for a new customer and predicts their estimated churn probability.

Example output:

```text
Prediction: Customer may churn
Churn probability: 73.04%
```

This probability is an estimate from the model, not a guarantee that the customer will leave.

## What I Learned

- Loading and exploring a dataset using Pandas
- Handling missing and non-numeric data
- Converting categorical columns into dummy variables
- Splitting data into training and testing sets
- Scaling features using StandardScaler
- Training a Logistic Regression model
- Evaluating a model using accuracy, recall, F1-score, and a confusion matrix
- Using predicted probabilities and a custom decision threshold
- Making predictions for a new customer

## How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:

```bash
pip install pandas scikit-learn
```

3. Make sure `data.csv` is in the project folder.
4. Run the Python script:

```bash
python main.py
```

## Future Improvements

- Improve the model's predictions.
- Compare different classification models.
- Explore additional customer features.

---

**Project Status:** Beginner Machine Learning project completed for learning and practice.
