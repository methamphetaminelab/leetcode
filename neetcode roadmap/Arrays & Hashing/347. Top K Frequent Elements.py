class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        smap = {}
        for num in nums:
            if num in smap:
                smap[num] += 1
            else:
                smap[num] = 1
        
        sortedMap = sorted(smap.items(), key=lambda x: x[1], reverse=True)

        result = [item[0] for item in sortedMap[:k]]

        return result