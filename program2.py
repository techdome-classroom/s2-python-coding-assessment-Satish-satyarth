class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        def isValid(s: str) -> bool:
    # Dictionary to match closing and opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Stack to hold opening brackets
    stack = []

    # Loop through each character in the string
    for char in s:
        if char in bracket_map:
            # Pop the top element from stack if it's non-empty, else assign a dummy value
            top_element = stack.pop() if stack else '#'
            
            # If the mapping for this closing bracket doesn't match the stack's top element
            if bracket_map[char] != top_element:
                return False
        else:
            # Push the opening bracket onto the stack
            stack.append(char)
    
    # If the stack is empty, all brackets were matched; otherwise, it's invalid
    return not stack

# Test cases
print(isValid("()"))       # Output: True
print(isValid("()[]{}"))   # Output: True
print(isValid("(]"))       # Output: False
print(isValid("([)]"))     # Output: False
print(isValid("{[]}"))     # Output: True

        pass



