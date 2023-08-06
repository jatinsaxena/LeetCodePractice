class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # It can be done by just returining s[::-1]
        # But will be writting custom Logic
        
        
        start = 0 
        end = len(s) - 1
        
        while(start<end):
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            
            start+=1
            end-=1
        
        return s