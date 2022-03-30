'''
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105


Approach 1:
    Algo: We can use Selection sort to solve this problem. It takes O(n^2) Time Complexity and O(1) Space Complexity

    class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums),0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    start = min(start,i)
                    end = max(end,j)
        if end-1 < 0:
            return 0
        else:
            return end-start+1

Approach 2:
    Algo:
    Copy whole input array into another array
    Sort the whole array
    Traverse both the arrays at a time. If elements in both the arrays are equal, just increment the index. Initalize start =len(nums) en edn=0. 
    If elements in the input array are greater, update start with start = min(start,i)  and end with end = max(end,j). At last return end-start+1

    class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums),0
        sorted_nums = nums[:]
        sorted_nums.sort()
        for i in range(len(nums)):
            if sorted_nums[i]!= nums[i]:
                start = min(start,i)
                end = max(end,i)
        if end - start>=0:
            return end - start +1
        else:
            return 0
    This takes O(nlogn) Time Complexity and O(n) Space Complexity

Approach 3:
    Algo:
    Using stack, we can find position of min and max element of unsorted subarray
    Traverse array two times
        Find position of min element of unsorted subarray by traversing from left to right
        Find position of max element of unsorted subarray by traversing from right to left
'''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start, end =len(nums), 0
        #Traverse From left to right
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start,stack.pop())
            stack.append(i)
        # Traverse from right to left
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end,stack.pop())
            stack.append(i)
        if end - start>0:
            return end-start+1
        else:
            return 0
            
            
        
        