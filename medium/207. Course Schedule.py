class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        queue = []

        for course, pre in prerequisites:
            indegrees[course] += 1
            adjacency[pre].append(course)
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)  # 将没有pre的课程加入queue
        
        while queue:
            pre = queue.pop()
            numCourses -= 1
            for course in adjacency[pre]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        
        return numCourses == 0
        
