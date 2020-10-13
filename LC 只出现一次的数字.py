from functools import reduce

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

    def singleNumber1(self, nums):
        '''
        reduce函数 [1,2,3] -> 1+2 = 3 ,3+3 = 6
        :param nums:
        :return:
        '''
        return reduce(lambda x, y: x ^ y, nums)

a = [1, 2, 4, 2, 1]
b = Solution().singleNumber1(a)
print(b)