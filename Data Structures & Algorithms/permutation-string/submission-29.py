class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
            col = {}
            dic = {}
            for i in s1:
                col[i]= 1 + col.get(i,0)

            hay = False
            have, want = 0, len(col)
            lent = len(s1)
            l=0
            for r in range(len(s2)):
            
                if s2[r] in col:

                    dic[s2[r]] = 1 + dic.get(s2[r],0)

                    if dic[s2[r]] == col[s2[r]]:
                        have = have + 1

                if r-l +1> len(s1):
                    if s2[l] in dic:
                        if dic[s2[l]] == col[s2[l]]:
                            have = have - 1
                    
                        dic[s2[l]] = dic[s2[l]]-1

                    l = l+1

                if have == want:
                        hay = True

            return hay
                