from algorithms.classes import Agent, ItemState, Allocation
from algorithms.tools import NOTIONS, get_pareto_efficiency, get_total_utility


def find_constraints(allocation: Allocation):
    '''O(m+2*n) number of constraints: items and each pair of agents (WEF)
       With fractional allocations, each agent should have no less utlity than others.
       And item fractions should sum up to one.
    '''
    pass

class LPSolver:
    def __init__(self, allocation: Allocation):
        ## Constraints
        ## Objectives (maximize Nash welfare, best Pareto efficiency)
        

        # TODO: find constraints, objective functions
        # TODO: implement several LP algorithms and compare performances (converging speed, etc.)
        # TODO: set up a website that enables **real-time** updates and user trials
        pass
