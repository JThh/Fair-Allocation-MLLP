"""
Add boosts to uniform distribution to generator numbers for agent preferences toward items.
Number of agents and items are from a Poission distributions. 

Generator:
- Draw number of agents and agent preferences from a particular distribution
- Make sure that number of items exceed number of agents by O(/n)
- Possibly run on food bank problem in a previous paper to test out the effect
- Online learning: solicit a round of agent preferences after each optimization completes (boosts)
"""