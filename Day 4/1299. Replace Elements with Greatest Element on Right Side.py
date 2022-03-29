'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
Example 2:

Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 105

Approach 1: Bruteforce Approach
    Algo:
    Pick one element and compare it with the remaining (n-1) elements
    Return the maximum element towards right i.e from the i+1 index
    class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n =len(arr)
        for i in range(n):
            max_element = -1
            for j in range(i+1,n):
                if arr[j] > max_element:
                    max_element  = arr[j]
            arr[i] = max_element
        return arr
        #Time limit exceed error

        This take O(n^2) Time Complexity and O(1) Space Complexity


Approach 2:
    Algo:
    Traverse form right to left
    Initially assign last index with -1
    Take max_element_seen_sofar variable and intitalize it with -1
    Compare and update with the maximum element using temporary variable

    This takes O(n) Time Complexity and O(1) Space Complexity

'''

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_element_seen_so_far = arr[n-1]
        max_element_seen_so_far = -1
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = max_element_seen_so_far
            if temp > max_element_seen_so_far:
                max_element_seen_so_far = temp
        return arr
        