class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        dic = {}
        for i in range(0,length):
            temp = target - nums[i]
            if (dic.__contains__(temp)):
                if i<=dic[temp]:
                    return [i,dic[temp]]
                else:
                    return [dic[temp],i]
            dic[nums[i]] = i