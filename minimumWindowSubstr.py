class Solution:
    def minWindow(self, s: str, t: str) -> str:
        frq={}
        if len(s)<len(t) or not s or not t:
            return ''
        for ch in t:
            if ch in frq:
                frq[ch]+=1
            else:
                frq[ch]=1
        have = 0
        need = len(frq)
        window={}
        left = 0
        res=""
        res_len=float("inf")
        for right,ch in enumerate(s):
            window[ch]=window.get(ch,0)+1
            if ch in frq and window[ch]== frq[ch]:
                have+=1
        
            while have == need:
                if (right-left+1)<res_len:
                    res=s[left:right+1]
                    res_len = right-left+1
                window[s[left]]-=1
                if s[left] in frq and window[s[left]]<frq[s[left]]:
                    have-=1
                left+=1
        return res
        
