"""
Problem 26: Remove Duplicates
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""

#Solution 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
        
        return i 
