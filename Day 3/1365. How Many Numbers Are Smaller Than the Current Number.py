'''
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100

Approach 1: Brute Force
    Algo:
    For every element, compare it with remaining element
    Count it and return the resultant count array
    This takes O(n^2) Time Complexity and O(1) Space Complexity.

Approach 2: Using Hashtable
    Sort the input Array
    Construct HashMap
    Traverse the entire input array and return the corresponding value
    
    class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count  = { }
        for key, value in enumerate(sorted(nums)):
            if value not in count:
                count[value] = key
        return [count[value] for value in nums]

    This takes O(nlogn) Time Complexity and O(n) Space Complexity

Approach 3: Using Prefix Sum
    Algo:
        Construct an ArrayList of given size
        Traverse input array and count number of occurances
        Make a prefix sum and update each position
        Traverse the array, go through each indices, whatever value present before that index in the cell, keep it in the resultant.

'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #Construct ArrayList, traverse the input array and count the occurances
        count = [0]*101
        for value in nums:
            count[value] += 1
        #Compute prefix sum
        for i in range(1,101):
            count[i] += count[i-1]
        #Traverse and compute result
        result = [0] * len(nums)
        for key, value in enumerate(nums):
            if value>0:
                result[key] = count[value-1]
        return result
            
        