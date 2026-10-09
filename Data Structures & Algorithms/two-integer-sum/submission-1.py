class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            if (target-nums[i]) in count: 
                return sorted([i, count.get(target-nums[i])])
            count[nums[i]] = i

        