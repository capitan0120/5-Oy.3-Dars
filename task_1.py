from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        v = []
        for i in range(len(nums)-1):
            k = target-nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == k:
                    v.append(i)
                    v.append(j)
                    return v
