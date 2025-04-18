import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn

def bessel_up(x, lmax):
    """向上递推计算球贝塞尔函数
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
        
    Returns:
        numpy.ndarray, 从0到lmax阶的球贝塞尔函数值
    """
    # 学生在此实现向上递推算法
    # 提示:
    # 1. 初始化结果数组
    # 2. 计算j_0和j_1的初始值
    # 3. 使用递推公式计算高阶项
    
    j = np.zeros(lmax + 1)
    
    j[0] = np.sin(x) / x if x != 0 else 1.0  # j_0(x)
    
    if lmax > 0:
        j[1] = np.sin(x) / x**2 - np.cos(x) / x  # j_1(x)

    for l in range(1, lmax):
        j[l+1] = (2*l + 1) / x * j[l] - j[l-1]
    
    return j

def bessel_down(x, lmax, m_start=None):
    """向下递推计算球贝塞尔函数
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
        m_start: int, 起始阶数，默认为lmax + 15
        
    Returns:
        numpy.ndarray, 从0到lmax阶的球贝塞尔函数值
    """
    # 学生在此实现向下递推算法
    # 提示:
    # 1. 设置足够高的起始阶数
    # 2. 初始化临时数组并设置初始值
    # 3. 使用递推公式向下计算
    # 4. 使用j_0(x)进行归一化
    
    if m_start is None:
       m_start = lmax + 15

    j_temp = np.zeros(m_start + 2)

    j_temp[m_start+1] = 0.0
    j_temp[m_start] = 1.0
    
    for l in range(m_start, 0, -1):
        j_temp[l-1] = (2*l + 1) / x * j_temp[l] - j_temp[l+1]
    
    j0_analytic = np.sin(x) / x if x != 0 else 1.0

    scale = j0_analytic / j_temp[0]
    j = j_temp[:lmax+1] * scale
    
    return j

    
def plot_comparison(x, lmax):
    """绘制不同方法计算结果的比较图
    
    Args:
        x: float, 自变量
        lmax: int, 最大阶数
    """
    # 学生在此实现绘图功能
    # 提示:
    # 1. 计算三种方法的结果
    # 2. 绘制函数值的半对数图
    # 3. 绘制相对误差的半对数图
    # 4. 添加图例、标签和标题
   
    j_up = bessel_up(x, lmax)
    j_down = bessel_down(x, lmax)
    l = np.arange(lmax + 1)
    j_scipy = spherical_jn(l, x)
    
    plt.figure(figsize=(10, 6))
    plt.semilogy(range(lmax + 1), np.abs(j_up), 'o-', label='Push upwards')
    plt.semilogy(range(lmax + 1), np.abs(j_down), 's-', label='Push downwards')
    plt.semilogy(range(lmax + 1), np.abs(j_scipy), 'x-', label='Scipy reference value')
    plt.xlabel('order l')
    plt.ylabel('|j_l(x)|')
    plt.title(f'Comparison of spherical Bezier function values (x = {x})')
    plt.legend()
    plt.grid(True)
    
    plt.savefig(f'bessel_comparison_x{x:.1f}.png') 
    plt.show()

    plt.figure(figsize=(10, 6))
    
    relative_error_up = np.where(j_scipy != 0, np.abs((j_up - j_scipy) / j_scipy), 0)
    relative_error_down = np.where(j_scipy != 0, np.abs((j_down - j_scipy) / j_scipy), 0)
    
    plt.semilogy(range(lmax + 1), np.abs((j_up - j_scipy) / j_scipy), 'o-', label='Push the relative error upward')
    plt.semilogy(range(lmax + 1), np.abs((j_down - j_scipy) / j_scipy), 's-', label='Push the relative error downward')
    plt.xlabel('order l')
    plt.ylabel('relative error')
    plt.title(f'Comparison of relative errors of spherical Bezier functions (x = {x})')
    plt.legend()
    plt.grid(True)
    
    plt.savefig(f'bessel_error_x{x:.1f}.png') 
    plt.show()

def main():
    """主函数"""
    # 设置参数
    lmax = 25
    x_values = [0.1, 1.0, 10.0]
    
    # 对每个x值进行计算和绘图
    for x in x_values:
        plot_comparison(x, lmax)
        
        # 打印特定阶数的结果
        l_check = [3, 5, 8]
        print(f"\nx = {x}:")
        print("l\tUp\t\tDown\t\tScipy")
        print("-" * 50)
        for l in l_check:
            j_up = bessel_up(x, l)[l]
            j_down = bessel_down(x, l)[l]
            j_scipy = spherical_jn(l, x)
            print(f"{l}\t{j_up:.6e}\t{j_down:.6e}\t{j_scipy:.6e}")

if __name__ == "__main__":
    main()
