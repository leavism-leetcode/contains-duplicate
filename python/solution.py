"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for number in nums:
            if number in seen:
                return True
            seen.add(number)
        return False
    
# Instantiate the Solution class
solution = Solution()

# Test data
test_data1 = [1, 2, 3, 1]
test_data2 = [1, 2, 3, 4]
test_data3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

# Call the containsDuplicate method with the test data
result1 = solution.containsDuplicate(test_data1)
result2 = solution.containsDuplicate(test_data2)
result3 = solution.containsDuplicate(test_data3)

# Print the results
print(f"Test data 1: {test_data1}, Output: {result1}")
print(f"Test data 2: {test_data2}, Output: {result2}")
print(f"Test data 3: {test_data3}, Output: {result3}")
