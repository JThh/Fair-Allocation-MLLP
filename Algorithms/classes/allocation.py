from typing import List

from algorithms.classes.agent import Agent
from algorithms.classes.item import ItemState, get_allocation_from_states


class Allocation:
    '''Stores the overall scheme of allocation'''
    def __init__(self, agents: List[Agent], items: List[ItemState]):
        self.agents = agents
        self.items = items
        allocations = get_allocation_from_states(self.items)
        
        for (i, agent) in enumerate(self.agents):
            agent.set_allocation(allocations[i])
            
        print("Allocations set.")
