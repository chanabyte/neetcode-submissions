class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i, 0) + 1
        sortit = sorted(mp.items(), key = lambda pair: pair[1], reverse = True)
        return [num for num, freq in sortit[:k] ]