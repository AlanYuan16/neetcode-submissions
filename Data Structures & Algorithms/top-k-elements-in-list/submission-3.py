class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # We are using a has map to count the occurance of each value
        bucket = [[] for i in range(len(nums) + 1)] # need to off set because it starts at 0

        for val in nums:
            count[val] = count.get(val, 0) + 1
        # This maps the value to the number of occurance

        for num, freq in count.items():
            bucket[freq].append(num)
        res = []

        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res