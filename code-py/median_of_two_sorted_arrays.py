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

算法思想:
    Step 1. 将问题转换为找第 k(k>1) 小的元素; 由输入的 l1 和 l2 俩个数组均为从小到大排序的有序数组, 可比较 v1=l1[k/2 - 1] 与 v2=l2[k/2 - 1] (此处要考虑数据越界)
    Step 2. 如果 v1 <= v2: l1 的前 k/2 - 1 个元素不可能为第k小的元素, 向后移动索引标记位 index_l1 k/2个以排除元素; 并缩小 k(减去排除的元素个数)
                v1 > v2: l2 的前 k/2 - 1 个元素不可能为第k小的元素, 向后移动索引标记位 index_l2 k/2个以排除元素; 并缩小 k(减去排除的元素个数)
    Step 3. 循环 Step 2 过程直至满足一下退出条件:
            若 index_l1 = len(l1) l1 为空/查找完毕, l2[index_l2 + k -1] 即为第k小的元素
            若 index_l2 = len(l2) l2 为空/查找完毕, l1[index_l1 + k -1] 即为第k小的元素
            若 k == 1 则 min(l1[index_l1], l2[index_l2]) 为第k小的元素
"""

import this
from typing import List

# class Solution
print("##### Start - O(log(m+n)) #####")
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    def findK(k: int):
        index_l, index_r = 0, 0
        
        while True:
            # 查找结束判断
            if index_l == nums1_len :   # nums1 为空/已经找完
                return nums2[index_r + k -1]
            if index_r == nums2_len :   # nums2 为空/已经找完
                return nums1[index_l + k -1]
            if k == 1 : # 查找结束
                return min(nums1[index_l], nums2[index_r])

            index_l_l = min(index_l + k // 2 - 1, nums1_len - 1) # 重置查找的起始位置
            index_r_r = min(index_r + k // 2 - 1, nums2_len - 1)
            v1, v2 = nums1[index_l_l], nums2[index_r_r]
            if v1 <= v2 :
                k -= index_l_l - index_l + 1
                index_l = index_l_l + 1
            else:
                k -= index_r_r - index_r + 1
                index_r = index_r_r + 1

        
    nums1_len = len(nums1)
    nums2_len = len(nums2)
    total_len = nums1_len + nums2_len

    if total_len % 2 == 1 :
        ''' 奇数项 '''
        return findK((total_len + 1) // 2)
    else : 
        ''' 偶数项 '''
        return (findK(total_len // 2) + findK(total_len // 2 + 1)) / 2.0

nums1 = [1,2]
nums2 = [3,4]
result = findMedianSortedArrays(this, nums1, nums2)
print("nums1 = [1,2] and nums2 = [3,4] 的中位数为:{0}".format(result))
print("##### End - O(log(m+n)) #####")


print("##### Start - O(m+n) #####")
def findMedianSortedArrays_1(self, nums1: List[int], nums2: List[int]) -> float:
    len_l1 = len(nums1)
    len_l2 = len(nums2)
    len_total = len_l1 + len_l2
    index_l1, index_l2 = 0, 0
    l = []

    while index_l1 < len_l1 and index_l2 < len_l2:
        if nums1[index_l1] <= nums2[index_l2] :
            l.append(nums1[index_l1])
            index_l1 += 1
        else :
            l.append(nums2[index_l2])
            index_l2 += 1

    if len_l1 > index_l1 :
        l = l + nums1[index_l1:]
    
    if len_l2 > index_l2 :
        l = l + nums2[index_l2:]

    if len_total % 2 == 1 :
        ''' 奇数项 '''
        return l[len_total // 2]
    else : 
        ''' 偶数项 '''
        return (l[len_total // 2 - 1] + l[len_total // 2]) / 2.0

    return None

nums1 = [1,2]
nums2 = [3,4]
result = findMedianSortedArrays_1(this, nums1, nums2)
print("nums1 = [1,2] and nums2 = [3,4] 的中位数为:{0}".format(result))
print("##### End - O(log(m+n)) #####")

print("##### Start - 代码简洁的写法 #####")
def findMedianSortedArrays_2(self, nums1: List[int], nums2: List[int]) -> float:
    l = nums1 + nums2
    l.sort()

    if len(l) % 2 == 1 :
        ''' 奇数项 '''
        return l[len(l) // 2]
    else : 
        ''' 偶数项 '''
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

    return None

nums1 = [1,2]
nums2 = [3,4]
result = findMedianSortedArrays_2(this, nums1, nums2)
print("nums1 = [1,2] and nums2 = [3,4] 的中位数为:{0}".format(result))
print("##### End - 代码简洁的写法 #####")