class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        res = []

        for i in range(len(nums), -1, -1):
            if buckets[i]:
                for n in buckets[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
        return res