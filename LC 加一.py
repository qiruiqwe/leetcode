class Solution(object):
    # 输入数字，输出字符数组
    def plusOne(self, digits):
        """
        第一个想法：
        把数字转化为字符
        把字符存数组中
        然后转化为数字
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = str(digits)
        return [int(i) for i in list(digits)]

    # 字符串转化的方式
    def plusOne1(self, digits):
        newstr = ''
        # list -> str
        for i in digits:
            newstr += str(i)
        # str -> int
        newnum = int(newstr)
        newnum += 1
        # int -> str
        newnewstr = str(newnum)
        newlst = []
        # str -> list
        for i in newnewstr:
            newlst.append(int(i))
        return newlst

    # 数字加法，从后往前加1
    def plusOne2(self, digits):
        digits.pop()
        print(digits)
        length = len(digits) - 1
        flag = True
        while length >= 0 and flag:
            if digits[length] + 1 < 10:
                digits[length] += 1
                flag = False
            else:
                digits[length] = 0
                length -= 1
        if length < 0:
            digits.insert(0, 1)
        return digits

    # list使用数组名 直接可以判断是不是空
    def plusOne3(self, digits):
        newlst = []
        # 从后往前是9则删除，添加0
        # 循环推出条件是 数组为空或最后一位不是9
        while digits and digits[-1] == 9:
            digits.pop()
            newlst.append(0)
        if not digits:
            return [1] + newlst
        else:
            digits[-1] +=1
            return digits +newlst

        return digits


a = Solution().plusOne2([])
print(a)
