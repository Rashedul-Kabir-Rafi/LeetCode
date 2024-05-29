class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sub_list = [s[i:i+k] for i in range(0, len(s),k)]
        final_list=[]
        for i,j in enumerate(sub_list):
            if i % 2 == 0:
                final_list.append(j[::-1])
            else:
                final_list.append(j)
        return "".join(final_list)