'''
You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].

The number of global inversions is the number of the different pairs (i, j) where:

0 <= i < j < n
nums[i] > nums[j]
The number of local inversions is the number of indices i where:

0 <= i < n - 1
nums[i] > nums[i + 1]
Return true if the number of global inversions is equal to the number of local inversions.

 

Example 1:

Input: nums = [1,0,2]
Output: true
Explanation: There is 1 global inversion and 1 local inversion.
Example 2:

Input: nums = [1,2,0]
Output: false
Explanation: There are 2 global inversions and 1 local inversion.
 

Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i] < n
All the integers of nums are unique.
nums is a permutation of all the numbers in the range [0, n - 1].


Approach 1: Bruteforce Approach
    Algo:
    c = 0
    for i = 0 to n-1:
        for j = i+1 to n-2:
            if i<j and A[i] > A[j]:
                c ++
This takes O(n^2) Time Complexity and O(1) Space Complexity.

Approach 2: We can use variation of Mergesort. This takes O(nlogn) Time Complexity and O(nlogn) Space Complexity

'''
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        c=A[0]       
        for i in range(len(A)-2):
            if A[i] > c:
                c=A[i]
            if c > A[i+2]:
                return False 
        return True