## Pair problem (income distribution)

We have a collection of 1874 incomes saved in `incomes.csv`, as well as whether or not that individual has a (post-high school) degree.

We are interested in finding the median income of the population, as well as determining a good logistic regression model for predicting whether someone has a degree or not based on their income. Instead of getting point estimates, we are also interested in the "typical error" of our estimates. We will use a technique called bootstrapping to estimate our error.


### 1. Finding the median income, and its distribution

Repeat the following procedure 200 times:
* Generate a sample of 1874 _with replacement_ from the list of incomes
* Calculate the median of each sample
Since our 1874 incomes are a sample of the whole population, we can simulate the error sampling induces on the median by "sampling" on our sample.

Once you have done this, make a histogram showing the distribution of your 200 estimates of the median. You know what the "true" median of the sample is; add that on with a dotted line. Also tell me the 2.5th percentile and 97.5th percentile for the median -- this gives us a range where the median appeared in 95% of your samples.

### 2. Finding the logistic regression coefficients

We want to model the probability of getting a degree using logistic regression, which depends on two coefficients:
P(degree) = 1/(1 + exp(-y)),   y = m*(income) + b*(1)

Here is our bootstrapping procedure:
* Take 200 samples of 1874 _with replacement_ from our data.
* Use `sklearn`'s LogisticRegression to fit a model to your sample
* Store the coefficient and intercept from your LogisticRegression into a list or array called `coefficients` and `intercepts`, respectively
When you are done, `coefficients` and `intercepts` should contain your 200 coefficients and intercepts.

Once you have done this, use
```python
import seaborn as sns
sns.jointplot( coefficients, intercepts, size=10)
```