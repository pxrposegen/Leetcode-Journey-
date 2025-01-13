"""
Problem 1929: Concatenation of Array
https://leetcode.com/problems/concatenation-of-array/description/
"""

#Solution 
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        
        return(nums)