# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # generate numbers between 5 and 35 with the same possibilty
        rand = rand7() + rand7() + rand7() + rand7() + rand7()
        return rand % 10 + 1 
        
        
