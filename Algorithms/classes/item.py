from enum import Enum
from typing import List

from allocation_table import AllocationTable


class ItemState:
    def __init__(self, fractions: List[float]):
        if abs(sum(fractions) - 1.0) <= 1e-2:
            print(f'Charity amount: {abs(sum(fractions) - 1.0)}')
        self.charity = abs(sum(fractions) - 1.0)  # proportion that get unallocated
        self.fractions = fractions
        self.len = len(self.fractions)

    @classmethod
    def empty_state(length: int):
        assert length > 0
        return ItemState([1.0] + [0.0] * (length - 1))
    
    
def get_allocation_from_states(states: List[ItemState]) -> List[AllocationTable]:
    assert all([state.len == states[0].len for state in states])
    n_item = len(states)
    n_agent = states[0].len
    table = [[0.0] * n_item for _ in range(n_agent)]
    
    for (i, state) in enumerate(states):
        for (j, fraction) in enumerate(state.fractions):
            table[j][i] = fraction
            
    table = [AllocationTable(l) for l in table]
    return table


class Item:
    ItemType: Enum
    
    def __init__(self, types: List[str], init_state: ItemState = None):
        self.ItemType = Enum('ItemType', types)
        self.state = init_state
        
    def set_state(self, state: ItemState):
        self.state = state
