"""
Problem 1700: Number of students unable to eat Lunch 
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/
"""

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        total = len(students)
        preferred = Counter(students)

        for i in sandwiches: 
            if preferred[i] > 0: 
                preferred[i] -= 1
                total -= 1
            else: 
                return total 

        return total 