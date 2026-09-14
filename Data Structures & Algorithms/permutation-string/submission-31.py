class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

            if len(s1)>len(s2):
                return False


            list1, list2 = [0]*26,[0]*26

            for i in range(len(s1)):
                list1[ord(s1[i])-ord('a')] += 1
                list2[ord(s2[i])-ord('a')] += 1

            have = 0 

            for i in range(26):
                if list1[i] == list2[i]:
                    have += 1
            l = 0
            for i in range(len(s1),len(s2)):
                
                if have == 26:
                    return True
                
                list2[ord(s2[i])-ord('a')] += 1
                if list2[ord(s2[i])-ord('a')] == list1[ord(s2[i])-ord('a')]:
                    have +=1
                elif list2[ord(s2[i])-ord('a')] -1 == list1[ord(s2[i])-ord('a')]:
                    have -=1


                list2[ord(s2[l])-ord('a')] -= 1
                if list2[ord(s2[l])-ord('a')] == list1[ord(s2[l])-ord('a')]:
                    have +=1
                elif list2[ord(s2[l])-ord('a')]+1 == list1[ord(s2[l])-ord('a')]:
                    have -=1

                l+=1
            



            return have == 26
                