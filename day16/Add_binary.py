class Solution:
    def add_binary(self, a: str, b: str) -> str:
        result = []
        carry = 0

        # Make both strings the same length by padding with zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Add from the rightmost bit to the left
        for i in range(max_len - 1, -1, -1):
            total = carry + int(a[i]) + int(b[i])
            result.append(str(total % 2))  # binary result bit
            carry = total // 2             # update carry

        # If there's still a carry, append it
        if carry:
            result.append('1')

        # Reverse to get the final binary string
        return ''.join(reversed(result))

sol=Solution()
a="11"
b="1"
res=sol.add_binary(a,b)
print(res)