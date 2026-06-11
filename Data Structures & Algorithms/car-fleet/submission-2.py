class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort cars descending ( largest position first )
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        list.sort(cars, reverse=True)

        stack = []
        print(f'cars: {cars}')
        for curr in range(len(position)):
            position = cars[curr][0]
            speed = cars[curr][1]
            time = (target - position) / speed
            print(f'time: {time} target: {target} position: {position} speed: {speed}')
            if not stack or time > stack[-1]:
                stack.append(time)
            else:
                pass
        print(f'stack: {stack}')
        return len(stack)

        # We can use a set to track how many unique times there has been for fleets
        # We need to consider the point were cars can reach each other even before the ending target
