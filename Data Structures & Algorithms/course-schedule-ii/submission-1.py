class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ordering = []
        adj = defaultdict(list)
        indegrees = defaultdict(int)
        for (course, prereq) in prerequisites:
            adj[prereq].append(course)
            indegrees[course] += 1
        bfs = deque([i for i in range(numCourses) if not indegrees[i]])
        while bfs:
            curr = bfs.pop()
            ordering.append(curr)
            for neighbor in adj[curr]:
                indegrees[neighbor] -= 1
                if not indegrees[neighbor]:
                    bfs.append(neighbor)
        return ordering if len(ordering) == numCourses else []
        