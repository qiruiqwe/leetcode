# @Time : 2020/10/18 22:50
# @Author : 亓瑞
# @File : LC 两数之和.py
# @desc :
class Solution:
    def twoSum(self, nums, target):
        '''
        哈希表中存贮遍历过去的数字和位置
        后面的数据的差值在hash表中搜索
        :param nums:
        :param target:
        :return:
        '''
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i
            print(hashtable)


a = [2, 7, 11, 15]
target = 9
b = Solution().twoSum(a, target)
print(b)
