from algorithms.classes.allocation_table import AllocationTable, UtilityTable


class Agent:

    def __init__(self,
                 utility_table: UtilityTable,
                 weight: float,
                 init_allocation: AllocationTable = None
                 ):
        self.utility_table = utility_table
        self.weight = weight
        self.utility = 0.0
        if init_allocation:
            assert init_allocation.len == utility_table.len, "Keep the number of items consistent"
            self.utility = Agent.get_utility(self.utility_table, init_allocation)
            self.allocation = init_allocation

    @staticmethod
    def get_utility(table: UtilityTable, allocation: AllocationTable) -> float:
        utility = 0.0
        for (i, allocation_ratio) in enumerate(allocation.allocation_table):
            utility += allocation_ratio * table[i]
        return utility

    def set_allocation(self, allocation: AllocationTable):
        assert allocation.len == self.utility_table.len, "Keep the number of items consistent"
        self.allocation = allocation
        self.utility = Agent.get_utility(self.utility_table, self.allocation)

