import math 

class Solution:
    def isPalindrome(self, x):
        if x<0:
            return False
        #number of digits
        digit = int(math.log10(x))
        masker = pow(10, digit)
        
        #until there is only 1 
        while(x>10):
            #if the first and last digit number is not the same it is not a palindrome
            if x%10 != x//masker:
                return False
            #remove first and last digit
            x = (x//10)% (masker//10)
            #divide masker for 100 to skip the last two digits compared
            masker = masker//100

        return True
        