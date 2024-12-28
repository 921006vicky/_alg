import numpy as np

# 定義要積分的函數
def compute_function(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

# 方法1: 使用黎曼和進行積分計算
def riemann_sum_method(N):
    dx, dy, dz = 1.0 / N, 1.0 / N, 1.0 / N
    sum_result = 0.0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                x = (i + 0.5) * dx
                y = (j + 0.5) * dy
                z = (k + 0.5) * dz
                sum_result += compute_function(x, y, z) * dx * dy * dz
    return sum_result

# 方法2: 使用蒙地卡羅法進行積分估算
def monte_carlo_method(M):
    x_values = np.random.uniform(0, 1, M)
    y_values = np.random.uniform(0, 1, M)
    z_values = np.random.uniform(0, 1, M)
    function_results = compute_function(x_values, y_values, z_values)
    volume = 1.0  # 單位立方體的體積
    return np.mean(function_results) * volume

# 設置分割數量與隨機樣本數量
riemann_partitions = 100  # 黎曼法的分割數
monte_carlo_samples = 1000  # 蒙地卡羅法的樣本數

# 計算積分結果
riemann_output = riemann_sum_method(riemann_partitions)
monte_carlo_output = monte_carlo_method(monte_carlo_samples)

# 打印積分結果
print(f"黎曼和法結果 (N={riemann_partitions}): {riemann_output}")
print(f"蒙地卡羅法結果 (M={monte_carlo_samples}): {monte_carlo_output}")
