# -*- coding: utf-8 -*-
# @Time : 2020/3/19 10:30
# @Author : wangmengmeng
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

class Solution1:
    """该算法会提示 超出时间限制 ，不推荐"""
    def twoSum(self, nums, target):
        a_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    a_list.append(i)
                    a_list.append(j)
        return a_list

class Solution2:
    def twoSum(self, nums, target):
        res_list = []
        for x in range(len(nums)):
            a = target - nums[x]
            if a in nums and x != nums.index(a):
                res_list.append(x)
                res_list.append(nums.index(a))
                return res_list


if __name__ == '__main__':
    ss = Solution2()
    nums = [2,7, 11, 15]
    target = 9
    print(ss.twoSum(nums,target))