import numpy as np
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1.排序
        nums = sorted(nums)
        print(nums)
        # 2.去重
        sort_num = sorted(list(set(nums)))
        print(sort_num)
        j = 1
        for i in range(len(sort_num)):
            if j > len(nums)-1:
                return sort_num[-1]
            if sort_num[i] == nums[j]:
                j = j + 2
                print(i, j)
            else:
                return sort_num[i]

a = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]

b = Solution().singleNumber(a)
print(b)