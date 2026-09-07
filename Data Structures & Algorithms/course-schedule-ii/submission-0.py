class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        indegrees = defaultdict(int)
        res = []
        for c in prerequisites:
            adj_list[c[1]].append(c[0])
            indegrees[c[0]] += 1
        bfs_q = deque()
        for c in range(numCourses):
            if indegrees[c] == 0:
                bfs_q.append(c)
        while bfs_q:
            course = bfs_q.popleft()
            res.append(course)
            for neighbor in adj_list[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    bfs_q.append(neighbor)
        if len(res) != numCourses:
            return []
        return res