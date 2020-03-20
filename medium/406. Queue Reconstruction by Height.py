class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))  # 对x[0]倒序，x[1]正序
        output = []
        for p in people:
            output.insert(p[1], p)  # 把p根据x[1]插入
        return output
