class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_lst = list(map(str, digits))
        num_str = ''.join(str_lst)
        
        chk_num = int(num_str) + 1
        res_str = list(str(chk_num))
        res = list(map(int, res_str))
        
        return res