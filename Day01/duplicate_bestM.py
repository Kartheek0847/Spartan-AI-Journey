class Solution(object):
    def containsDuplicate(self, nums):
        myset = set()
        for x in nums:
            if x in myset:
                return True
            myset.add(x)
        return False
           

        