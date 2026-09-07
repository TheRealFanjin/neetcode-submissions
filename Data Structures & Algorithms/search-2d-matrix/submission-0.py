class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m_i = 0
        m_j = len(matrix) - 1
        n_i = 0
        n_j = len(matrix[0]) - 1
        target_arr = -1
        while m_i <= m_j and n_i <= n_j:
            if target_arr == -1:
                mid = m_i + (m_j - m_i) // 2
                if matrix[mid][n_i] <= target <= matrix[mid][n_j]:
                    target_arr = mid
            
                if target < matrix[mid][n_i]:
                    m_j = mid - 1
                elif target > matrix[mid][n_j]:
                    m_i = mid + 1
            else:
                mid = n_i + (n_j - n_i) // 2
                if matrix[target_arr][mid] == target:
                    return True
                elif target < matrix[target_arr][mid]:
                    n_j = mid - 1
                elif target > matrix[target_arr][mid]:
                    n_i = mid + 1
        return False
        