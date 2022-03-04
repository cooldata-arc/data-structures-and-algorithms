"""
leetcode-url: 
    https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
desc:
    给定两个大小分别为 m 和 n 的正序(从小到大)数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数 。
    算法的时间复杂度应该为 O(log (m+n)) 。
example: 
    示例 1:
        输入: nums1 = [1,3], nums2 = [2]
        输出: 2.00000
        解释: 合并数组 = [1,2,3] , 中位数 2
    示例 2:
        输入: nums1 = [1,2], nums2 = [3,4]
        输出: 2.50000
        解释: 合并数组 = [1,2,3,4] , 中位数 (2 + 3) / 2 = 2.5
中位数:
    data: X,...,Xn   -> 从小到大排序
          当 n 为奇数时: m_0.5 = X_(n+1)/2
          当 n 为偶数时: m_0.5 = (X_(n/2) + X_(n/2 + 1)) / 2
"""

import re
from typing import List

# class Solution
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    nums1_len = nums1.__len__
    nums2_len = nums2.__len__
    total_len = nums1_len + nums2_len
    mod = total_len / 2

    if total_len % 2 == 1 :
        ''' 奇数项 '''
        if nums1_len == 0 and nums2_len == 0 :
            return None
        elif nums1_len == 0 :
            return nums2[mod] / 2.0
        else :
            return nums1[mod] / 2.0

        if nums1_len > nums2_len :
            s
        else :
            return 0.0
    else : 
        ''' 偶数项 '''
