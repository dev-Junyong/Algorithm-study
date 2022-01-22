class Solution:
    def isHappy(self, n: int) -> bool:
        st = set()
        cur = n
        prev = n
        
        while prev != 1:
            if prev in st:
                break
            
            st.add(prev)
            cur = prev
            prev = 0
            
            while cur:
                temp = cur % 10
                cur //= 10
                prev += temp**2
        return prev == True