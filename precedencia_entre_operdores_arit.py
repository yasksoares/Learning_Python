# 1. (n+n)
# 2. **
# 3. */ // %
# 4. + -

conta_1 = 1 + 1 ** 5 + 5 # 7
print(conta_1)

conta_1_2 = (1 + 1) ** (5 + 5)
print(conta_1_2)

conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_2)

print(conta_1_2 == conta_2)
print(conta_1 == conta_2)