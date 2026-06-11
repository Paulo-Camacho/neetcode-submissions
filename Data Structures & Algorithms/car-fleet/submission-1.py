class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We can use a set to track how many unique times there has been for fleets
        # We need to consider the point were cars can reach each other even before the ending target

        stack = []
        for curr in range(len(position)):
            stack.append((position[curr], speed[curr]))

        list.sort(stack, reverse=True)

        # I proved via the table that if the curr time is less than or lower than previous time it will join the fleet
        # else if curr is larger than previous time it makes a new fleet

        fleet = []
        # We use a stack to store the previous fleet
        for val in range(len(stack)):
            time = (target - stack[val][0]) / stack[val][1]
            print(f"stack[val] {stack[val]} time {time}")
            # If fleet is empty or current time is less than most advanced time*
            if not fleet or time > fleet[-1]:
                # If curr is larger than last this makes new fleet
                fleet.append(time)
            else:
                # I need to make the fleet join
                pass

        print(f'Fleet: {fleet}')
        return len(fleet)

