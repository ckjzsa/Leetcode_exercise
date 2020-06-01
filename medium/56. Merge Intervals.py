class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])
        res = []

        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                res[-1][1] = max(res[-1][1], interval[1])

        return res
