class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_copy = nums1[:m]
        index = 0
        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if num1_copy[p1] <= nums2[p2]:
                nums1[index] = num1_copy[p1]
                p1 += 1

            else:
                nums1[index] = nums2[p2]
                p2 += 1
            
            index += 1
        
        if p1 < m:
            for item in num1_copy[p1:]:
                nums1[index] = item
                index += 1
        elif p2 < n:
            for item in nums2[p2:]:
                nums1[index] = item
                index += 1




