# 方法 a
def power2n_a(n):
    return 2**n

# 方法 b：用遞迴
def power2n_b(n):
    if n == 0:
        return 1
    return power2n_b(n-1) + power2n_b(n-1)

# 方法 c：用遞迴
def power2n_c(n):
    if n == 0:
        return 1
    return 2 * power2n_c(n-1)

# 方法 d：用遞迴+查表
def power2n_d(n):
    # 初始化查表字典
    if not hasattr(power2n_d, 'table'):
        power2n_d.table = {0: 1}
    
    # 如果結果已在表中，直接返回
    if n in power2n_d.table:
        return power2n_d.table[n]
    
    # 否則計算結果，存入表中，然後返回
    result = power2n_d(n-1) + power2n_d(n-1)
    power2n_d.table[n] = result
    return result

print('power2n(40)=', power2n_d(40))