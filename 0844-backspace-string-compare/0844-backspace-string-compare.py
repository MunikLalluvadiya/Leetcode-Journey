class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        s_st = []

        for i in s:
            if i!="#":
                s_st.append(i)
            else:
                if len(s_st) != 0:
                    s_st.pop()
   

        t_st = []

        for i in t:
            if i!="#":
                t_st.append(i)
            else:
                if len(t_st) != 0:
                    t_st.pop()
       

        return s_st == t_st
