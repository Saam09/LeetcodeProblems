class Solution:
    def isPalindrome(self, x: int) -> bool:
#         list1 = list(map(int, str(x)))
#         k = 0
#         for i in list1[::-1]:
#             if(list[k]== i):
        return str(x)==str(x)[::-1]
