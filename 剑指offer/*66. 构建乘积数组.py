class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        left = [1] * len(a)
        right = [1] * len(a)
        for i in range(1, len(a)):
            left[i] = left[i-1] * a[i-1]
        
        for i in range(len(a)-2, -1, -1):
            right[i] = right[i+1] * a[i+1]

        for i in range(len(a)):
            left[i] = left[i] * right[i]
        
        return left
