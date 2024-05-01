class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        actualSum = 0
        for account in accounts:
            currentSum = 0
            for amt in account:
                currentSum += amt
            
            if currentSum > actualSum:
                actualSum = currentSum 
                
        return actualSum
        
        
object = Solution()

object.maximumWealth(accounts = [[1,5],[7,3],[3,5]])