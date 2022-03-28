'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000

Approach 1: BruteForce Approach
    Algo:
        Create to empty lists even_list and odd_list
        If elements in the array are even, append them to even_list else append them to the odd_list
        Return concatenation of even_list and odd_list

    This takes O(n) time complexity and O(n) Space Complexity

    class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even_list = []
        odd_list = []
        for numbers in nums:
            if numbers%2==0:
                even_list.append(numbers)
            else:
                odd_list.append(numbers)
        return even_list+odd_list

    class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [i for i in nums if nums%2==0] + [ i for in nums if nums%2!=0]


Approach 2: Two Pointer Approach
    Algo:
    Take two pointers such that
        i = 0
        j = len(nums) - 1
    Do this until i < j
        If nums[i] is odd, swap(nums[i],nums[j]) and decrement j
        Else increment i
    This takes O(n) Time Complexity and O(1) Space Time Complexity
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j =len(nums) - 1
        while(i<j):
            if nums[i]%2!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j = j-1
            else:
                i = i+1
        return nums
            
               
        