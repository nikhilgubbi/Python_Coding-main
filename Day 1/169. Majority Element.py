'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

Approach 1: We can use have Naive solution. It takes time complexity of O(n^2) and space complexity of O(1)
            Algo:
            for i=0 to n-1
                Store a[i]
                for j=0 to n-1
                    count elements
Approach 2: We can use hashtable to solve this. It takes O(n) time complexity but takes O(n) space complexity.

Approach 3: We can use Boyer-Moore Algorithm. This takes O(n) time Complexity and O(1) Space Complexity
            Algo:
            Boyer_Moore(Arr,n):
                int majority_ele
                int count = 0
                for i=0 to n-1:
                    if(count==0):
                        majority_ele = A[i]
                        count = count + 1
                    else 
                        if m ==A[i]
                            count++
                        else
                            count--
            Count the occurences if m occurs more than n/2 times
            If it has Occured, return the majority_ele
            Else Return Majority Element not Found 
            
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def findMajority(arr,n):
            major_element=0
            count=1
            for i in range(n):
                if arr[i]==major_element:
                    count+=1
                else:
                    count-=1
                if count==0:
                    major_element=arr[i]
                    count+=1
            return major_element
        def isMajority(arr,n,major_element):
            count=0
            for i in range(n):
                if arr[i]==major_element:
                    count+=1
            if count>n/2:
                return True
            else:
                return False
        if __name__=='__main__':
            arr=nums
            value=findMajority(arr,len(arr))
            if(isMajority(arr,len(arr),value)):
                return value
            else:
                print("Not Found")

        
        