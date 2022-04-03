'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

Approach 1: Bruteforce Approach 
    Algo:
        for i = 0 to n-1:
            for j =0 to i-1:
                find if there exists a[num] < a[i]
            for j =i +1 to n-1:
                find an element > a[i]

    This takes O(n^2) Time Complexity and O(1) Space Complexity

Approach 2:
    Algo:
        Start with maximum numbers for first and second element
            Find the first smallest number in the three subsequence
            Find the second one greater than the first element, reset the first one if its smaller.

    This takes O(n) Time Complexity and O(1) Space Complexity    
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstMin = float('inf')
        secondMin = float('inf')
        for itr, number in enumerate(nums):
            if number <= firstMin:
                firstMin = number
            elif number <= secondMin: 
                secondMin = number
            else:
                return True
        return False
        
        
        
        
        