class Solution:
    def longestConsecutive(self, mins: List[int]) -> int:
        # We are going to use a hashset to reduce time complexity
        nset = set(mins)
        print(f'This is nset : {nset}')
        longest = 0
        # We have the current smallest, now we can start iterating
        # In english add to set if value is ++ than smallest
        for curr in nset:
            if curr - 1 not in nset:
                # Let's start iterating from curr
                aset = set()
                aset.add(curr)
                proximo = curr + 1
                i = 0
                while i < len(nset):
                    if proximo in nset:
                        aset.add(proximo)
                        proximo += 1
                    i += 1
                    longest = max(len(aset), longest)
        return(longest)
