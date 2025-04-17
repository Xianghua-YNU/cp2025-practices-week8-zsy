import numpy as np

def standard_formula(a, b, c):
    """使用标准公式求解二次方程 ax^2 + bx + c = 0
    
    参数:
        a (float): 二次项系数
        b (float): 一次项系数
        c (float): 常数项
    
    返回:
        tuple: 方程的两个根 (x1, x2) 或 None(无实根)
    """
    # 学生在此处实现代码
    D = b**2 - 4*a*c
    
    if D < 0:
        return None
    sqrt_D = np.sqrt(D)
    x1 = (-b + sqrt_D) / (2*a)
    x2 = (-b - sqrt_D) / (2*a)
    
    return (x1, x2)


def alternative_formula(a, b, c):
    """使用替代公式求解二次方程 ax^2 + bx + c = 0
    该方法通过将标准公式的分子和分母都乘以 -b∓√(b^2-4ac) 得到
    
    参数:
        a (float): 二次项系数
        b (float): 一次项系数
        c (float): 常数项
    
    返回:
        tuple: 方程的两个根 (x1, x2) 或 None(无实根)
    """
    # 学生在此处实现代码
    D = b**2 - 4*a*c
    
    if D < 0:
        return None 
    
    sqrt_D = np.sqrt(D)
    
    x1 = (2 * c) / (-b - sqrt_D)
    x2 = (2 * c) / (-b + sqrt_D)
    
    return (x1, x2)


def stable_formula(a, b, c):
    """稳定的二次方程求根程序，能够处理各种特殊情况和数值稳定性问题
    
    参数:
        a (float): 二次项系数
        b (float): 一次项系数
        c (float): 常数项
    
    返回:
        tuple: 方程的两个根 (x1, x2) 或 None(无实根)
    """
    # 学生在此处实现代码
    if abs(a) < 1e-10:
        if abs(b) < 1e-10:  # a ≈ 0 且 b ≈ 0
            return None if abs(c) > 1e-10 else (0, 0)  
        return (-c/b, -c/b) 
    
    # 计算判别式
    D = b**2 - 4*a*c
    
    if D < 0:
        return None  # 无实根
    
    sqrt_D = np.sqrt(D)
    
    if b > 0:
        x1 = (-b - sqrt_D) / (2*a)
        x2 = (2*c) / (-b - sqrt_D)
    else:
        x1 = (-b + sqrt_D) / (2*a)
        x2 = (2*c) / (-b + sqrt_D)
    
    return (min(x1, x2), max(x1, x2)) if x1 != x2 else (x1, x2)

def main():
    test_cases = [
        (1, 2, 1),             # 简单情况
        (1, 1e5, 1),           # b远大于a和c
        (0.001, 1000, 0.001),  # 原测试用例
    ]
    
    for a, b, c in test_cases:
        print("\n" + "="*50)
        print("测试方程：{}x^2 + {}x + {} = 0".format(a, b, c))
        
        # 使用标准公式
        roots1 = standard_formula(a, b, c)
        print("\n方法1（标准公式）的结果：")
        if roots1:
            print("x1 = {:.15f}, x2 = {:.15f}".format(roots1[0], roots1[1]))
        else:
            print("无实根")
        
        # 使用替代公式
        roots2 = alternative_formula(a, b, c)
        print("\n方法2（替代公式）的结果：")
        if roots2:
            print("x1 = {:.15f}, x2 = {:.15f}".format(roots2[0], roots2[1]))
        else:
            print("无实根")
        
        # 使用稳定的求根程序
        roots3 = stable_formula(a, b, c)
        print("\n方法3（稳定求根程序）的结果：")
        if roots3:
            print("x1 = {:.15f}, x2 = {:.15f}".format(roots3[0], roots3[1]))
        else:
            print("无实根") 


if __name__ == "__main__":
    main()
