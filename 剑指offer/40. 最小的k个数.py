class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(arr) == 0:
            return []
            
        arr = sorted(arr)

        return arr[:k]
