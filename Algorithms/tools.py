from classes import Allocation

# __all__ = ['NOTIONS', 'get_pareto_efficiency']


def EF1():
    pass


def EF():
    pass


def PROP():
    pass


def PROP1():
    pass


def WEF1():
    pass


def WPROP1():
    pass


def WMMS():
    pass


def PMMS():
    pass


NOTIONS = {
    'EF1': EF1,
    'EF': EF,
    'PROP': PROP,
    'PROP1': PROP1,
    'WEF1': WEF1,
    'WPROP1': WPROP1,
    'WMMS': WMMS,
    'PMMS': PMMS
}


def get_total_utility(allocation: Allocation) -> float:
    agents = allocation.agents
    return sum([agent.utility for agent in agents])

def get_pareto_efficiency():
    pass
