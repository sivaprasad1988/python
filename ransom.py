class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        checkList = list(magazine)  # Create a list from magazine
        counter = 0
        for letter in ransomNote:
            for toCheck in checkList:
                if toCheck == letter:
                    counter += 1
                    checkList.pop(checkList.index(toCheck))
                    break
        return True if len(ransomNote) == counter else False

solution = Solution()
print(solution.canConstruct('fihjjjjei','hjibagacbhadfaefdjaeaebgi'))
