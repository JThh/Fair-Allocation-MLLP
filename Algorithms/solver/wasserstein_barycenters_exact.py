"""
Reference: https://github.com/eboix/high_precision_barycenters/
Find an implementation in C and make it an executable.

Finds a distribution/points such that the sum of its Wasserstein distances to each of a set of distributions/points would be minimised (thru self re-center and rotation).
The distances are actually the envy between agents (or utility differences) and distributional weights are actually the allocated items. (items are distributions)
It can be computed in polynomial time via LP-solver algorithm (code) in fixed dimensions (fixed number of agents).
"""