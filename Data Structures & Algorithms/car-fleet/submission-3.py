class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Lets make a list of tuples that are in descending order with position first
        tuples = []
        stack = []
        for i in range(len(position)):
            tuples.append((position[i], speed[i]))
        # We are sorting by the first memember inside of each individual tuple value
        tuples.sort(key=lambda x:x[0], reverse=True)
        # tuples.sort(reverse=True)

        for curr in range(len(position)):
            # I proved to myself that if a time is less than or equal to the car's fleet infront of it
            # it will join it otherwise it will make it's own fleet
            # Otherwise if the time is greater than the largest position that specific car is too
            # slow to catch up to this fleet
            time = ( target - tuples[curr][0]) / tuples[curr][1]
            print(f'time: {time}')
            # say we have time 3 3 3.5
            if not stack or time > stack[-1]:
                stack.append(time)
            else:
                pass
        return(len(stack))
        print(stack)
