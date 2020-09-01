# https://leetcode.com/problems/two-sum/

# wrong

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_1 in range(len(nums)):
            for idx_2 in range(idx_1, len(nums)):
                if (nums[idx_1] + nums[idx_2]) == target:
                    return [idx_1, idx_2]

# answer

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx_1 in range(len(nums)):
            for idx_2 in range((idx_1 + 1), len(nums)):
                if (nums[idx_1] + nums[idx_2]) == target:
                    return [idx_1, idx_2]