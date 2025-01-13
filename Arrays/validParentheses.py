"""
Problem 20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
"""

#Solution 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closingCharacter = {")" : "(", "]" : "[", "}" : "{"}

        for i in s: 
            if i in closingCharacter: 
                if stack and stack[-1] == closingCharacter[i]:
                    stack.pop()
                else: 
                    return False 
            else: 
                stack.append(i)

        return True if not stack else False