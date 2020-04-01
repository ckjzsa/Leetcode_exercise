class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 先排出现次数最多的任务，其他任务插入冷却时间，则为n*(maxt-1)，最多任务自身要maxt时间，
        # 最后加上其余一样多的任务数量

        tnum=[]
        for i in set(tasks):
            tnum.append(tasks.count(i))

        maxt=max(tnum)

        return max((maxt-1) * n + maxt + tnum.count(maxt) - 1, len(tasks))

