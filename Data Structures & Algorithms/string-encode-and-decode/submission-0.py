class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            # the idea is hold the lengh + # + word in a giant string
            #res += str(len(word)) + '#' + word
            res += f'{(len(word))}#{word}'

        print(res)
        return(res)



    def decode(self, s: str) -> List[str]:
        # we will decode the giant string and push back into a list
        answer_arr = []
        i = 0
        while (i < len(s)):
#          5#Hello5#Hello
            j = i
            while s[j] != '#':
                j += 1
            # we move j and grab the value right before #, this yields the number
            num = s[i:j]
            word = s[j + 1 : j + int(num) + 1]
            answer_arr.append(word)
            i = int(num) + 1 + j

        print(answer_arr)
        return(answer_arr)


        
            


