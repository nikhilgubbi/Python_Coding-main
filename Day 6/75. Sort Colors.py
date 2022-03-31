'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
 

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

Approach 1: We can use sorting algorithms such as QuickSort or MergeSort. It takes O(nlogn) Time complexity and O(1) Space Complexity

Approach 2: We can use two parses where first parse is to count the 0s,1s and 2s. Second parse to fill up the positions with the needed element

Approach 3:
    Algo:
        while(c!=h):
            if a[c] = 0:
                swap(a[c],a[l])
                c++
                l++
            if a[c] =1:
                c++
            else:
                swap(a[c],a[h])
                h--
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = l = 0
        h = len(nums) - 1
        while(c<=h):
            if nums[c]==0:
                nums[c],nums[l] = nums[l], nums[c]
                l = l+1
                c = c+1
            elif nums[c] ==1:
                c = c+1
            else:
                nums[c],nums[h] = nums[h],nums[c]
                h = h-1
        return nums
                
        