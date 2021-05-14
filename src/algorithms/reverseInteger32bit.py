class Solution:
    def reverse(self, x: int) -> int:
        if not x < 0:
            x = int(str(x)[::-1])
        else:
            x = int(str(x)[:1] + str(x)[1:][::-1])

        if x not in range((-1 << 31), (1 << 31) - 1):
            return 0
        return x

x = Solution()

# Sequencias de Testes
    # 123
    # -123
    # 120
    # 0
    # 1534236469

print(x.reverse(123))        # Tem que retornar => 321
print(x.reverse(-54321))     # Tem que retornar => -12345
print(x.reverse(120))        # Tem que retornar => 21
print(x.reverse(0))          # Tem que retornar => 0
print(x.reverse(1534236469)) # Tem que retornar => 0

