class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])
        for r in range(n):
            for c in range(m):
                if board[r][c] == 'O' and r not in [0, n - 1] and c not in [0, m - 1]:
                    dfs = [(r, c)]
                    visited = set([(r, c)])
                    surrounded = True
                    while dfs:
                        curr_r, curr_c = dfs.pop()
                        for (r_dir, c_dir) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            new_r, new_c = curr_r + r_dir, curr_c + c_dir
                            if 0 <= new_r < n and 0 <= new_c < m:
                                if (new_r in [0, n - 1] or new_c in [0, m - 1]) and board[new_r][new_c] == 'O':
                                    surrounded = False
                                    break
                                if board[new_r][new_c] == 'O' and (new_r, new_c) not in visited:
                                    visited.add((new_r, new_c))
                                    dfs.append((new_r, new_c))
                        if not surrounded:
                            break
                    if surrounded:
                        for (r1, c1) in list(visited):
                            board[r1][c1] = 'X'