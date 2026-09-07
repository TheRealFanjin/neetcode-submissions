class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(position[i], speed[i]) for i in range(len(position))]
        combined.sort(reverse=True)
        fleet_stack = []
        for car in combined:
            arrival = (target - car[0]) / car[1]
            if not fleet_stack or arrival > fleet_stack[-1]:
                fleet_stack.append(arrival)
        return len(fleet_stack)