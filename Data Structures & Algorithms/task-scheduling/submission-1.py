class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26
        for task in tasks:
            freqs[ord(task) - 65] += 1
        t = [(-freqs[i], i) for i in range(len(freqs)) if freqs[i]]
        heapq.heapify(t)
        counter = 0
        q = deque()
        while t or q:
            counter += 1
            if t:
                task = heapq.heappop(t)
                if task[0] != -1:
                    task = (task[0] + 1, task[1], counter + n)
                    q.append(task)
            if q and q[0][2] == counter:
                val = q.popleft()
                heapq.heappush(t, (val[0], val[1]))
        return counter
