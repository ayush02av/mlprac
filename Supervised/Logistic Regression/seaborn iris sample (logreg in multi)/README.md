# Seaborn IRIS Sample Dataset (Logistic Regression in Multi Variables)

## What
1. Used Seaborn Iris sample dataset for binary classification
2. Data Features:
    1. Independent:
        1. Sepal Length
        2. Sepal Width
        3. Petal Length
        4. Petal Width
    2. Dependent: Species
3. There were 3 kinds of species, but 1 was dropped for binary classification and simplification

## How
1. Used Seaborn.iris Dataset
2. Dropped one type of classified species
3. Used GridSearchCV for calculating best accuracy that can be achieved
    1. Used various parameters for various combinations of model like:
        1. Penalty
        2. C
        3. Max_iter
    2. This tests all the possible models and selects one with best accuracy

## What New
1. How to partially automate finding best accuracy
2. Using Seaborn