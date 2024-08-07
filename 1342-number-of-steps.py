class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = int(0)
        while num != 0:
            count += 1
            if num %2 == 0:
                num = num / 2
            elif num % 2 == 1:
                num = num - 1
        return count

object = Solution()
print( object.numberOfSteps(123) )