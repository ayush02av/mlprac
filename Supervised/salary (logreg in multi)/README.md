# Salary (Logistic Regression in Multi Variable)

## What
1. Logistic Regression for a multiclassified dataset
2. Data Features:
    1. 14 independent features like age, education, occupation, martial status etc.
    2. 1 binary classified dependent feature: income (<=50k, >50k)
3. Found model with number of features with best accuracy using Principal Component Analysis

## How
1. LabelEncoder
2. StandardScaler
3. PCA

## What New
1. How to use preprocessing modules for achieving optimal accuracy

## Doubts
1. After scaling down the data, how are future predictions done?
    1. For example, age feature is scaled down to 0-mean column
    2. Then how to predict for input age = 19 (example)
2. How to identify exactly what features were chosen for the model after PCA?