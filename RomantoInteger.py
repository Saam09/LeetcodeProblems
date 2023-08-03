class Solution:
    def romanToInt(self, s: str) -> int:
        c = 0
        for i in range(0,len(s)):
                if s[i]=="I":
                    c+=1
                elif s[i] =="V":
                    if s[i-1]=="I":
                        c+=3
                    else: 
                        c+=5
                elif s[i] =="X":
                    if s[i-1]=="I":
                        c+=8
                    else:
                        c+=10
                elif s[i] =="L":
                    c+=50
                elif s[i]=="C":
                    if s[i-1]=="X":
                        c+=80
                    else:
                        c+=100
                elif s[i]=="D":
                        c+=500
                elif s[i]=="M":
                    if s[i-1]=="C":
                        c+=800
                    else:
                        c+=1000
        return c
