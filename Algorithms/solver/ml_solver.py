"""
- Ideation: 
    - Treat each item as a feature and its value varies depending on allocation (while it sums to one)
    - The goal of the solver is to learn the weights for each item to each agent so that agents have roughly the same total weighted utility (or y-value)
    - Error function is the sample variance (mean squared error)
    - Ultimately trigger the integrator to `integralise` the solution
- Implementation:
    - Multi-class binary classification
    - The losses are sample variances
"""