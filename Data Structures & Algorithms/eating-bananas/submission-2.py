class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        minimum = 0
        while i <= j:
            mid = i + (j - i) // 2
            hour_counter = 0
            for k in piles:
                if k % mid == 0:
                    hour_counter +=  k // mid
                else:
                    hour_counter += k // mid + 1
                
                if hour_counter > h:
                    break
            if hour_counter > h:
                i = mid + 1
            else:
                minimum = mid
                j = mid - 1
        return minimum
        