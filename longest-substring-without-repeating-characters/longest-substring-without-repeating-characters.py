class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        sub_string = []
        start = 0
        end = 0
        
        while end < len(s):
            if s[end] not in sub_string:
                sub_string.append(s[end])
                max_length=max(max_length, len(sub_string))
                end+=1
            else:
                start = start+1
                end = start
                sub_string = []
                
            
        return max_length
            
        