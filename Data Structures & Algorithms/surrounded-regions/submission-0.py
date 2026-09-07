class Solution:
    def solve(self, board: List[List[str]]) -> None:
        not_surrounded = set()
        n = len(board)
        m = len(board[0])

        def bfs(r, c):
            nonlocal not_surrounded
            not_surrounded.add((r, c))
            bfs_q = deque([(r, c)])
            while bfs_q:
                curr_r, curr_c = bfs_q.pop()
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_r = curr_r + x
                    new_c = curr_c + y
                    if 0 <= new_r < n and 0 <= new_c < m and (new_r, new_c) not in not_surrounded and board[new_r][new_c] == 'O':
                        not_surrounded.add((new_r, new_c))
                        bfs_q.append((new_r, new_c))

        for r in range(n):
            if (r, 0) not in not_surrounded and board[r][0] == 'O':
                bfs(r, 0)
            if (r, m - 1) not in not_surrounded and board[r][m - 1] == 'O':
                bfs(r, m - 1)
        for c in range(m - 1):
            if (0, c) not in not_surrounded and board[0][c] == 'O':
                bfs(0, c)
            if (n - 1, c) not in not_surrounded and board[n - 1][c] == 'O':
                bfs(n - 1, c)
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and (r, c) not in not_surrounded:
                    board[r][c] = 'X'
         