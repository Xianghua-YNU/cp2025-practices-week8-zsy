import numpy as np
import matplotlib.pyplot as plt
import time

def f(x):
    """被积函数 f(x) = sqrt(1-x^2)
    
    参数:
        x (float): 输入值
        
    返回:
        float: 函数计算结果
    """
    # 学生在此实现被积函数
    return np.sqrt(1 - x**2)

def rectangle_method(f, a, b, N):
    """矩形法（左矩形法）计算积分
    
    参数:
        f (function): 被积函数
        a (float): 积分下限
        b (float): 积分上限
        N (int): 区间分割数
        
    返回:
        float: 积分近似值
    """
    # 学生在此实现矩形法
    # 提示:
    # 1. 计算步长 h = (b - a)/N
    # 2. 使用循环计算每个矩形的面积并累加
    h = (b - a) / N
    integral = 0.0
    for k in range(N):
        x_k = a + k * h
        integral += f(x_k) * h
    return integral

def trapezoid_method(f, a, b, N):
    """梯形法计算积分
    
    参数:
        f (function): 被积函数
        a (float): 积分下限
        b (float): 积分上限
        N (int): 区间分割数
        
    返回:
        float: 积分近似值
    """
    # 学生在此实现梯形法
    # 提示:
    # 1. 计算步长 h = (b - a)/N
    # 2. 使用循环计算每个梯形的面积并累加
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b)) * h
    for k in range(1, N):
        x_k = a + k * h
        integral += f(x_k) * h
    return integral

def calculate_errors(a, b, exact_value):
    """计算不同N值下各方法的误差
    
    参数:
        a (float): 积分下限
        b (float): 积分上限
        exact_value (float): 积分精确值
        
    返回:
        tuple: (N_values, h_values, rect_errors, trap_errors)
            N_values: 分割数列表
            h_values: 步长列表
            rect_errors: 矩形法误差列表
            trap_errors: 梯形法误差列表
    """
    # 学生在此实现误差计算
    # 提示:
    # 1. 定义不同的N值列表
    # 2. 对每个N值计算两种方法的积分近似值
    # 3. 计算相对误差 = |近似值 - 精确值| / |精确值|
    N_values = [10, 100, 1000, 10000]
    h_values = []
    rect_errors = []
    trap_errors = []
    
    for N in N_values:
        h = (b - a) / N
        h_values.append(h)
        
        rect_result = rectangle_method(f, a, b, N)
        trap_result = trapezoid_method(f, a, b, N)
        
        rect_error = abs(rect_result - exact_value) / exact_value
        trap_error = abs(trap_result - exact_value) / exact_value
        
        rect_errors.append(rect_error)
        trap_errors.append(trap_error)
    
    return N_values, h_values, rect_errors, trap_errors

def plot_errors(h_values, rect_errors, trap_errors):
    """绘制误差-步长关系图
    
    参数:
        h_values (list): 步长列表
        rect_errors (list): 矩形法误差列表
        trap_errors (list): 梯形法误差列表
    """
    # 学生在此实现绘图功能
    # 提示:
    # 1. 使用plt.loglog绘制双对数坐标图
    # 2. 添加参考线表示理论收敛阶数
    # 3. 添加图例、标题和坐标轴标签
    plt.figure(figsize=(10, 6))
    plt.loglog(h_values, rect_errors, 'o-', label='rectangle method')
    plt.loglog(h_values, trap_errors, 's-', label='trapezoidal method')
    
    # 添加参考线
    plt.loglog(h_values, [h**1 for h in h_values], '--', label='O(h)')
    plt.loglog(h_values, [h**2 for h in h_values], '--', label='O(h²)')
    
    plt.xlabel('step size h')
    plt.ylabel('relative error')
    plt.title('Error-step diagram')
    plt.legend()
    plt.grid(True)
    
    # 保存图表为 PNG 文件
    plt.savefig('error_convergence.png', dpi=300)
    plt.show()

def print_results(N_values, rect_results, trap_results, exact_value):
    """打印计算结果表格
    
    参数:
        N_values (list): 分割数列表
        rect_results (list): 矩形法结果列表
        trap_results (list): 梯形法结果列表
        exact_value (float): 精确值
    """
    # 学生在此实现结果打印
    # 提示: 格式化输出N值和对应积分结果
    print("\n计算结果表格:")
    print(f"{'N':<10}{'矩形法近似值':<20}{'梯形法近似值':<20}{'精确值':<20}")
    for i, N in enumerate(N_values):
        print(f"{N:<10}{rect_results[i]:<20.10f}{trap_results[i]:<20.10f}{exact_value:<20.10f}")


def time_performance_test(a, b, max_time=1.0):
    """测试在限定时间内各方法能达到的最高精度
    
    参数:
        a (float): 积分下限
        b (float): 积分上限
        max_time (float): 最大允许时间(秒)
    """
    # 学生在此实现性能测试
    # 提示:
    # 1. 从小的N值开始测试
    # 2. 逐步增加N值直到计算时间接近max_time
    # 3. 记录每种方法能达到的最高精度
    exact_value = 0.5 * np.pi
    N = 10
    rect_time = 0
    trap_time = 0
    
    while rect_time < max_time or trap_time < max_time:
       start_time = time.time()
        rectangle_method(f, a, b, N)
        rect_time = time.time() - start_time
        
        start_time = time.time()
        trapezoid_method(f, a, b, N)
        trap_time = time.time() - start_time
        
        if rect_time >= max_time or trap_time >= max_time:
            break
        
        N *= 10
        
     rect_result = rectangle_method(f, a, b, N)
     trap_result = trapezoid_method(f, a, b, N)
    
     rect_error = abs(rect_result - exact_value) / exact_value
     trap_error = abs(trap_result - exact_value) / exact_value
    
     print("\n时间性能测试结果:")
     print(f"矩形法在 {max_time} 秒内达到的最高精度: {rect_error:.10f} (N={N})")
     print(f"梯形法在 {max_time} 秒内达到的最高精度: {trap_error:.10f} (N={N})")


def calculate_convergence_rate(h_values, errors):
    """计算收敛阶数
    
    参数:
        h_values (list): 步长列表
        errors (list): 误差列表
        
    返回:
        float: 收敛阶数
    """
    # 学生在此实现收敛阶数计算
    # 提示: 使用最小二乘法拟合log(h)和log(error)的关系
    log_h = np.log(h_values)
    log_error = np.log(errors)
    
    # 使用最小二乘法拟合
    A = np.vstack([log_h, np.ones(len(log_h))]).T
    slope, _ = np.linalg.lstsq(A, log_error, rcond=None)[0]
    
    return slope

def main():
    """主函数"""
    a, b = -1.0, 1.0  # 积分区间
    exact_value = 0.5 * np.pi  # 精确值
    
    print(f"计算积分 ∫_{a}^{b} √(1-x²) dx")
    print(f"精确值: {exact_value:.10f}")
    
    # 计算不同N值下的结果
    N_values = [10, 100, 1000, 10000]
    rect_results = []
    trap_results = []
    
    for N in N_values:
        rect_results.append(rectangle_method(f, a, b, N))
        trap_results.append(trapezoid_method(f, a, b, N))
    
    # 打印结果
    print_results(N_values, rect_results, trap_results, exact_value)
    
    # 计算误差
    _, h_values, rect_errors, trap_errors = calculate_errors(a, b, exact_value)
    
    # 绘制误差图
    plot_errors(h_values, rect_errors, trap_errors)
    
    # 计算收敛阶数
    rect_rate = calculate_convergence_rate(h_values, rect_errors)
    trap_rate = calculate_convergence_rate(h_values, trap_errors)
    
    print("\n收敛阶数分析:")
    print(f"矩形法: {rect_rate:.2f}")
    print(f"梯形法: {trap_rate:.2f}")
    
    # 时间性能测试
    time_performance_test(a, b)

if __name__ == "__main__":
    main()
