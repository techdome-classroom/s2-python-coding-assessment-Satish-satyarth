class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary for Roman numeral values
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        # Loop through the Roman numeral string
        for i in range(len(s)):
            # If the current Roman numeral is smaller than the next one, subtract it
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                total -= roman_dict[s[i]]
            else:
                # Otherwise, add its value to the total
                total += roman_dict[s[i]]

        return total

# The isValid function is now separate from the Solution class
def isValid(s: str) -> bool:
    
    bracket_map = {')': '(', '}': '{', ']': '['}

    
    stack = []

    
    for char in s:
        if char in bracket_map:
            
            top_element = stack.pop() if stack else '#'

            
            if bracket_map[char] != top_element:
                return False
        else:
            
            stack.append(char)

    
    return not stack