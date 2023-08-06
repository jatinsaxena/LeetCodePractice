class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string_array = []
        
        for character in s:
            if character.isalnum():
                cleaned_string_array.append(character.lower())
        
        if "".join(cleaned_string_array) != "".join(cleaned_string_array[::-1]):
            return False
        
        return True
        
        
        
        
        