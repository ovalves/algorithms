class Solution:
    def reverse(self, x: int) -> int:
        if not x < 0:
            x = int(str(x)[::-1])
        else:
            x = int(str(x)[:1] + str(x)[1:][::-1])

        if x not in range((-1 << 31), (1 << 31) - 1):
            return 0
        return x