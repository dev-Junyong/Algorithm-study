class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = s.upper().replace('-','')
        flag = len(res) % k
        ans = []
        if flag > 0:
            ans.append(res[:flag])
        temp = flag
        while temp < len(res):
            ans.append(res[temp:temp+k])
            temp += k
        return '-'.join(ans)