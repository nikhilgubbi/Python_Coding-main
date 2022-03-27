'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Approach 1: Polynomial Time
        Algo: rotateOnceArray(A,n):
            temp = A[n-1]
            for i = n-2 to 0:
                A[i+1] = A[i]
            A[0] = temp

        Apply the rotateOnceArray function k Times. This takes O(n*k) time complexity and O(1) Space Complexity

Approach 2: Linear TIme + Additional TIme Complexity
        Algo 
        Copy last k elements into temp
        Move n-k-1 elements to destination array
        Copy everything in temp back to the destination array

        This takes O(n+k) time complexity and O(k) space Complexity

Approach 3: 
    Algo 
        Reverse the k array elements
        Reverse the n-k array elements
        Reverse the whole array elements

        This takes O(n) time complexity and O(1) Space Complexity
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr,i,j):
            while(i<=j):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i = i+1
                j = j-1
        def rotateKtimes(arr,n,k):
            reverse(arr,n-k,n-1)
            reverse(arr,0,n-k-1)
            reverse(arr,0,n-1)
            print(arr)
            
        if __name__=='__main__':
            arr = nums
            n = len(arr)
            k = k % n
            rotateKtimes(arr,n,k)
        
            

    
        