class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26 # [0,0...0] 26 0s

            for char in word:
                count[ord(char) - ord("a")] += 1
                # "abad" -> [2,1,0,1]

            print('current word:', word)
            print('count:',count)
            
            result[tuple(count)].append(word)
        return result.values()

