# <Python Algorithm Interview> 180p CH7 no.8
# https://leetcode.com/problems/trapping-rain-water/

from typing import List

# answer_1
def trap1(height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), \
                              max(height[right], right_max) # update left_max, right_max
        
        # left_max and right_max are going to be met at highest point
        if left_max <= right_max:
            volume += left_max - height[left] # water depth
            left += 1 # move left pointer
        else:
            volume += right_max - height[right] # water depth
            right -= 1 # move right pointer
    
    return volume

# answer_2
def trap2(height: List[int]) -> int:
    