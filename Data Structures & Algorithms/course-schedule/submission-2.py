class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegrees = defaultdict(int)
        for (course, prereq) in prerequisites:
            adj_list[prereq].append(course)
            indegrees[course] += 1
        bfs = deque([i for i in range(numCourses) if indegrees[i] == 0])
        course_count = 0
        while bfs:
            course = bfs.popleft()
            course_count += 1
            for neighbor in adj_list[course]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    bfs.append(neighbor)
        return course_count == numCourses