import numpy as np
import matplotlib.pyplot as plt

def sum_up(N):
    """从小到大计算调和级数和
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 调和级数和
    """
    # 学生在此实现从小到大求和
    # 提示: 使用循环从1加到N，每次加上1/n
    total = 0.0
    for n in range(1, N+1):
        total += 1.0 / n
    return total

def sum_down(N):
    """从大到小计算调和级数和
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 调和级数和
    """
    # 学生在此实现从大到小求和
    # 提示: 使用循环从N减到1，每次加上1/n
    total = 0.0
    for n in range(N, 0, -1):
        total += 1.0 / n
    return total

def calculate_relative_difference(N):
    """计算两种方法的相对差异
    
    参数:
        N (int): 求和项数
        
    返回:
        float: 相对差异值
    """
    # 学生在此实现相对差异计算
    # 提示: 使用公式 |S_up - S_down| / ((S_up + S_down)/2)
    s_up = sum_up(N)
    s_down = sum_down(N)
    
    if s_up + s_down == 0:
        return 0.0
    
    return abs(s_up - s_down) / ((s_up + s_down) / 2)
    
def plot_differences():
    """绘制相对差异随N的变化"""
    # 学生在此实现绘图功能
    # 提示:
    # 1. 使用np.logspace生成N值
    # 2. 计算每个N对应的相对差异
    # 3. 使用plt.loglog绘制双对数坐标图
    N_values = np.logspace(1, 4, 50, dtype=int)
    
    relative_differences = [calculate_relative_difference(N) for N in N_values]
    
    plt.figure(figsize=(10, 6))
    plt.loglog(N_values, relative_differences, 'b-o', markersize=5, alpha=0.7)
    plt.xlabel('N (number of terms)', fontsize=12)
    plt.ylabel('relative differences δ', fontsize=12)
    plt.title('The influence of the summation order of harmonic series on relative differences', fontsize=14)
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.tight_layout()
    
    plt.savefig('relative_difference_vs_N.png')
    plt.show()


def print_results():
    """打印典型N值的计算结果"""
    # 学生在此实现结果打印
    # 提示:
    # 1. 选择几个典型N值(如10,100,1000,10000)
    # 2. 计算并格式化输出两种方法的和及相对差异
    test_N = [10, 100, 1000, 10000]
    
    print(f"{'N':<10} | {'S_up':<20} | {'S_down':<20} | {'相对差异 δ':<20}")
    print("-" * 70)
    
    for N in test_N:
        s_up = sum_up(N)
        s_down = sum_down(N)
        delta = calculate_relative_difference(N)
        
        print(f"{N:<10} | {s_up:<20.15f} | {s_down:<20.15f} | {delta:<20.15f}")

def main():
    """主函数"""
    # 打印计算结果
    print_results()
    
    # 绘制误差图
    plot_differences()

if __name__ == "__main__":
    main()
