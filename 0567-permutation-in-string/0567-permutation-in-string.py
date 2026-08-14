class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window={}
        need={}
        for c in s1:
            need[c]=need.get(c,0)+1
        
        i=0
        for j in range(len(s2)):
            window[s2[j]]=window.get(s2[j],0)+1

            if j-i+1>len(s1):
                window[s2[i]]-=1

                if window[s2[i]]==0:
                    del window[s2[i]]
                i+=1
#check if the current window is permuation or not
            if j - i + 1 == len(s1):
                if window == need:
                    return True
        return False
                

