"""
Problem 682: Baseball Game
https://leetcode.com/problems/baseball-game/description/
"""

#Solution 
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = list()
        for i in operations: 
            if i.lstrip("-").isdigit(): 
                result.append(int(i))

            elif i == "+":
                result.append((result[-1] + result[-2]))
            
            elif i == "D":
                result.append((result[-1] * 2))
            
            elif i == "C":
                result.pop()
            
        return (sum(result))