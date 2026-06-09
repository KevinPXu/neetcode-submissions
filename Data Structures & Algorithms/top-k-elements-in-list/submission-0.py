class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for key, value in counts.items():
            buckets[value].append(key)
        output = []
        for i in reversed(buckets):
            for num in i:
                output.append(num)
                
                if len(output) == k:
                    return output
        
