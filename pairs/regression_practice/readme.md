# Pair Problem: Regression

Explore a [practice dataset](Practice_data.csv) by implementing a linear regression in five steps:

1) Plot each independent variable against the dependent variable and take note of any obvious relationships. Seaborn regplots can help!

2) Split into a training set and a test set.

3) Build a few regression models using `sm.OLS` and the training set, trying to improve performance each time.

4) According to these models, what can you say about the sign and certainty of the relationships between the variables in the data?  Do the independent variables have a linear relationship with the dependent variable?

5) Apply the results of each of these regression models to predict the test sample.  Compare the models using the adjusted R2 - which model performs the best in the test sample?