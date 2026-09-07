class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            position[i] = [position[i], speed[i]]
        position = sorted(position, reverse=True)

        fleet_stack = [(target - position[0][0]) / position[0][1]]
        for i in range(1, len(position)):
             if (target - position[i][0]) / position[i][1] > fleet_stack[-1]:
                fleet_stack.append((target - position[i][0]) / position[i][1])
        
        return len(fleet_stack)


        