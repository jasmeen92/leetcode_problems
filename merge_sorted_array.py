'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
 

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''


class Solution: # two pointers, one for iterating through the array, and one for writing the next non-val element
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None: # iterate through the array with i, and write non-val elements to index k
        p1 = m - 1 # pointer for the last element in nums1 (the last non-zero element)
        p2 = n - 1 # pointer for the last element in nums2
        write = m + n - 1 # pointer for writing the next largest element to the end of nums1

        while p2 >= 0: # while there are still elements in nums2 to merge
            if p1 >= 0 and nums1[p1] > nums2[p2]: # if the current element in nums1 is larger than the current element in nums2, write it to index write and decrement p1
                nums1[write] = nums1[p1] # write the larger element from nums1 to index write
                p1 -= 1 # decrement p1 to point to the next element in nums1
            else: # if the current element in nums2 is larger than or equal to the current element in nums1, write it to index write and decrement p2
                nums1[write] = nums2[p2] # write the larger element from nums2 to index write
                p2 -= 1 # decrement p2 to point to the next element in nums2
            write -= 1 # decrement write to point to the next index for writing