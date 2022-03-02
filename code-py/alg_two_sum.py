"""
url: https://leetcode-cn.com/problems/two-sum/
给定一个整数数组 nums 和一个整数目标值 target,请你在该数组中找出和为目标值 target 的那两个整数,并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是,数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1:
输入: nums = [2,7,11,15], target = 9
输出: [0,1]
解释: 因为 nums[0] + nums[1] == 9 ,返回 [0, 1] 。

示例 2:
输入: nums = [3,2,4], target = 6
输出: [1,2]

示例 3:
输入: nums = [3,3], target = 6
输出: [0,1]

"""

import this
from typing import List

# class Solution:
def twoSum(self, nums: List[int], target: int) -> List[int]:
    result=[]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                result.append(i)
                result.append(j)
                return result

def hashTwoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    a = []
    for i in range(len(nums)):
        a.append(target - nums[i])
    for j in range(len(nums)):
        if nums[j] == a[j] :
            a[j] = None
        if nums[j] in a:
            result.append(j)
            result.append(a.index[nums[j]])
            return result

def truningHashTwoSum(self, nums: List[int], target: int) -> List[int]:
    result = []
    a = dict()
    for i in range(len(nums)):
        if a.get(nums[i], -1) != -1:
            result.append(a.get(nums[i]))
            result.append(i)
            return result
        a[target - nums[i]] = i
    return result

def truningHashTwoSum2(self, nums: List[int], target: int) -> List[int]:
    result = []
    a = []
    for i in range(len(nums)):
        if nums[i] in a:
            result.append(a.index(nums[i]))
            result.append(i)
            return result
        a.append(target - nums[i])
    return result

nums = [2,7,11,15]
target = 9
print("truningHashTwoSum:[0,1] ", truningHashTwoSum(this, nums, target))
print("truningHashTwoSum:[1,2] ", truningHashTwoSum(this, [3,2,4], 6))
print("truningHashTwoSum:[1,2] ", truningHashTwoSum(this, [2,5,5,11], 10))

print("truningHashTwoSum2:[0,1] ", truningHashTwoSum(this, nums, target))