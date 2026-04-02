class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            word_len = len(word)
            encoded_string = encoded_string+str(word_len)+'#'+word
        #print(encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        str_list = []
        i = 0
        j = 0
        while j < len(s):
            if s[j]=='#':
                prefix_len = int(s[i:j])
                str_list.append(s[j+1:j+1+prefix_len])
                i = j+1+prefix_len
                j=i
            else:
                j+=1
        return str_list



