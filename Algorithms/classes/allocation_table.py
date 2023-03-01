import math
from typing import List


class AllocationTable:
    def __init__(self, allocation_table: List[float]):
        for num in allocation_table:
            assert num >= 0.0 and num <= 1.0, "only fractional allocation is feasible"
        self.allocation_table = allocation_table
        self.len = len(allocation_table)


class UtilityTable:
    def __init__(self, table: List[float]):
        for num in table:
            assert num != -math.inf and num != math.inf
        self.utility_table = table
        self.len = len(table)
