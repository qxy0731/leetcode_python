class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_hash = {}
        for i in range(len(nums)):
            if nums[i] not in my_hash:
                my_hash[target - nums[i]] = i
            else:
                return my_hash[nums[i]],i
