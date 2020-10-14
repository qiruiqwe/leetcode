from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 先排序，找到长度最小的list，对其元素进行遍历
        # 在另一个数组中查找有无相同的元素，有则删除同时加入交集
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        if len(nums2) < len(nums1):
            temp = nums2
            nums2 = nums1
            nums1 = temp
        unite = []
        for i in nums1:
            if i in nums2:
                unite.append(i)
                nums2.remove(i)
        return unite

    def intersect1(self, nums1, nums2):
        # Counter 进行计数，获得每个元素的
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        # counter类型求交集
        num = nums1 & nums2
        # elements 将其中的key值乘以出现的次数全部打印出来
        return list(num.elements())

    def intersect2(self, nums1, nums2):
        '''
        哈希表法
        :param nums1:
        :param nums2:
        :return:
        '''
        # 这波操作太骚了，这样的置换减少了中间变量的使用
        # 最小数组维 nums1
        if len(nums1) > len(nums2):
            return self.intersect2(nums2, nums1)
        m = Counter(nums1)
        unit = []
        for num in nums2:
            if m[num] > 0:
                unit.append(num)
                m[num] -= 1
        return unit

a = [1, 2, 4, 2, 1]
b = [2, 4]
b = Solution().intersect2(a, b)
print(b)