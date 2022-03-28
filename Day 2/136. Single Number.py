'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.


Approach 1: Bruteforce 
    Algo:
    for i = 0 to n-1:
        count = 0 
        for j = 0 to n-1:
            if a[i] == a[j]:
                count+ =1
        if count%2!=0:
            return a[i]
    return -1 

    This takes O(n^2) Time Complexity and O(1) Space Complexity

Approach 2: Using Hashtable 
    Algo: 
    Create Hash Function
    Store the hash of the function in Hash Table
    When the same element occurs, increement and store the count
    Retun the element which has occured odd number of times

    This takes O(n) Time Complexity but takes O(n) Space Complexity since we are using Hastable

from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        
        for i in hash_table:
            if hash_table[i] == 1:
                return i

Approach 3: Using XOR
    Algo:
    ans = 0
    for i = 0 to n-1:
        ans = ans ^ i
    return i

    This takes O(n) Time Complexity and O(1) Space Complexity            
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans = ans ^ i
        return ans