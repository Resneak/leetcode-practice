class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # First, check if a solution is possible
        if sum(gas) < sum(cost):
            return -1
        
        total_gas = 0
        current_gas = 0
        start_index = 0
        
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            
            # If current_gas becomes negative, reset the start point to the next station
            if current_gas < 0:
                start_index = i + 1
                current_gas = 0
        
        return start_index