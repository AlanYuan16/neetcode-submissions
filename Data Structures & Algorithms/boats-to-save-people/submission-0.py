class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        sorted_arr = sorted(people)
        res = 0
        left, right = 0, len(people) - 1
        

        while left <= right:
            if sorted_arr[left] + sorted_arr[right] > limit:
                right -= 1
                res += 1
            else:
                res += 1
                right -= 1
                left +=1
        return res
        
          