class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashy = {}
        for i in range(len(strs)):
            word = strs[i]
            ordered = "".join(sorted(word))
            if ordered in hashy:
                hashy[ordered].append(word)
            else:
                hashy[ordered] = [word]
            
        print(hashy)
        print(hashy.values())
        return(list(hashy.values()))
