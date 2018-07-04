class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_hash = {}
        for i in range(len(nums)):
            if nums[i] in my_hash:
                return my_hash[nums[i]],i
            else:
                my_hash[target - nums[i]] = i
