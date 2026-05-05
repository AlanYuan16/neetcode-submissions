class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Phase 1: Count frequencies
        # 1. Count frequency
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for val in nums:
            count[val] = count.get(val, 0) + 1
        # frequency map → top k elements

        # 2. Bucket sort by frequency
        for num, freq in count.items():
            bucket[freq].append(num)
        
        result = []

        for i in range(len(nums), -1 , -1):
            if bucket[i]:
                for n in bucket[i]:
                    result.append(n)
                    if len(result) == k:
                        return result
        return result
            
