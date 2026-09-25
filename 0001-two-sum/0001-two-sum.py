class Solution(object):

    def twoSum(self, nums, target):
        vistos = {}

        for i, num in enumerate(nums):
            complemento = target - num

            if complemento in vistos:
                return [vistos[complemento], i]

            vistos[num] = i