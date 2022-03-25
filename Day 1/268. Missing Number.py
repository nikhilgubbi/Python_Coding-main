'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''

'''
Approach 1 : We can use Linear Search. It takes time complexity of O(n^2) and space complexity of O(1)

Approach 2 : We can use sum of n numbers formula
            Algo:
            MN(arr,n):
                sum = n * (n+1)
                for i=0 to n-2:
                    sum = sum - a[i]
                return sum

                But there is a catch in this since there would be a problem of Overflow when using other programming languages


Approach 3 : We can use Xor operation i.e,  0^0=0 , 0^1=1 , 1^0=1 , 1^1=0
            Algo:
            MN(arr,n):
                int a = 0
                for i=1 to n:
                    a = a XOR i
                b = 0
                for i=0 to n-2:
                    b = b XOR a[i]
                return a ^ b

                This use O(n) Time Complexity and O(1) time Complexity

'''

# Implementation

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)):
            xor = xor ^ (i+1) ^ nums[i]
        return xor