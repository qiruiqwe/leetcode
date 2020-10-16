class Solution(object):

    def moveZeroes(self, nums):
        """
        remove 和 index 当找不到时都是返回异常
        count 找到0的个数
        remove 去除0元素
        append 添加0元素
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero_num = nums.count(0)
        # for i in nums:
        #     if i == 0:
        #         zero_num += 1
        for i in range(zero_num):
            nums.remove(0)
            nums.append(0)
        return nums

    def moveZeroes2(self, nums):
        '''
        使用慢指针，i为0元素的位置，j为非零元素的位置，两者交换
        i为慢指针，每次移动1
        :param nums:
        :return:
        '''
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return nums

a = [1, 0, 1]
b = Solution().moveZeroes2(a)
print(b)