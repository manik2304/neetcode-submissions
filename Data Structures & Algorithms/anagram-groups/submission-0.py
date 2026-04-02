class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        l = len(strs)

        if l == 0 or l==1:
            return [strs]

        my_dict = {}
        for word in strs:
            key = self.make_key(word) # it is a tuple
            group = my_dict.get(key,[])
            group.append(word)
            my_dict[key] = group
        return list(my_dict.values())


    def make_key(self, word: str) -> Tuple[int]:
        key = [0]*26

        for char in word:
            ind = ord(char)-ord('a')
            key[ind] += 1

        return tuple(key)