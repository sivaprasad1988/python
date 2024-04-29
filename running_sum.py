class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        sum = 0
        for num in nums:
            sum += num
            runningSum.append(sum)
        return runningSum
    
object = Solution()

object.runningSum(nums = [1,2,3,4])    