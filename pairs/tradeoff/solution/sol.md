**What is the bias/variance trade-off?**

(very short directions for answers)

- Can you explain in simple terms what this is?
  - These describe a model's flexibility to learn new things.
  - High bias: the model is relatively fixed in what it can learn. These tend toward underfitting.
  - Low bias: the model has a lot of room to fit to the data. These tend to overfit.
- How does it affect modeling decisions?
  - Choose higher bias models when data is noisy, higher variance when you have higher quality and more data.
- How does it relate to model complexity?
  - More complex models tend to be higher variance.
- How do various models compare?
  - LinReg: High bias
  - LogReg: High bias
  - SVM: High bias-high variance
  - CART: High bias-high variance
  - RF: High bias-high variance
  - NB: High bias
  - Deep learning: High bias-high variance
- How do you assess and address the issue?
  - Cross validation is the main tool for addressing the issue. With cross validation we can get a sense for how sensitive a model's performance is to which examples are included. Many models have hyperparameters that allow us to tune the complexity and thus bias/variance: regularization parameters, depth for RF.
