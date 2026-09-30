class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        arr1, arr2 = [0] * 26, [0] * 26
        # mark the array in terms of the ascii value
        for i in range(len(s1)):
            # from the start of a
            arr1[ ord(s1[i]) - ord('a') ] += 1
            arr2[ ord(s2[i]) - ord('a') ] += 1

        left = 0
        # we are making a window of size one and moving it until the last valid member
        for right in range(len(s1), len(s2)):
            print(f'arr1 {arr1}')
            print(f'arr2 {arr2}')
            matches = 0
            for i in range(26):
                matches += 1 if arr1[i] == arr2[i] else 0
            print(matches)
            if matches == 26:
                return True

            # Now update
            left2 = ord(s2[left]) - ord('a') 
            arr2[left2] -= 1
            index = ord(s2[right]) - ord('a') 
            arr2[index] += 1
            # index = ord(s2[right]) - ord('a') 
            # arr2[index] += 1
            # if arr1[index] == arr2[index]:
            #     matches += 1
            # elif arr1[index] + 1 == arr2[index]:
            #     matches -= 1
            
            # # now we are dealing with the left side of the window
            # index = ord(s2[left]) - ord('a')
            # arr2[index] -= 1
            # if arr2[index] == arr1[index]:
            #     matches += 1
            # elif arr2[index] - 1 == arr1[index]:
            #     matches -= 1
            left += 1


        matches = 0
        for i in range(26):
            matches += 1 if arr1[i] == arr2[i] else 0
        return matches == 26