'''

Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

 

Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.
 

Example 2:

Input:
n = 5
A[] = {1,2,3,4,0}
Output: 4 0
 

Your Task:
You don't need to read input or print anything. The task is to complete the function leader() which takes array A and n as input parameters and returns an array of leaders in order of their appearance.

 

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

 

Constraints:
1 <= n <= 107
0 <= Ai <= 107


Approach 1: Bruteforce
    Algo:
    for i = 0 to n-1:
        for j = i+1 to n-1:
            if a[i] < a[j]:
                a[i] is not a leader in the array
        a[i] is a leader in the array
    This approach takes O(n^2) Time Complexity and O(1) Space Complexity.

Approach 2: Using Curretnt Max and travelling from right to left
    Algo:
    findLeaders(A,n):
    current_Max = -infinity
    for i = n-1 to 0:
        if a[i] >current_Max:
            print a[i]
            current_Max = a[i]
    This approach takes O(n) Time Complexity and O(1) Space Complexity
'''

import sys
def findLeaders(arr,n):
    max_value=-sys.maxsize -1
    for i in range(n-1,-1,-1):
        if(max_value<arr[i]):
            max_value=arr[i]
            print(max_value)
        
findLeaders([16, 17, 4, 3, 5, 2],6)        

