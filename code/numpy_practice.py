import numpy as np
import sys
sys.stdout.reconfigure(encoding='utf-8')
try:

    yields = np.arange(25.0,105.0,5.0)
    print(yields)
    max_yield = np.max(yields)
    print(f"最大值：{str(max_yield)}")

    
    mean_yield = np.mean(yields)
    print(f"平均值：{str(mean_yield)}") 
    print("平均值：" + str(mean_yield))

    #单位换算
    temperatures = yields + 273.15
    print(temperatures)
    #标准差
    std_yield = np.std(yields)

    upper_bound = mean_yield + 2 * std_yield
    lower_bound = mean_yield - 2 * std_yield

    outliers = yields[(yields > upper_bound) | (yields < lower_bound)]
    #[()|()],[()&()]
    print(f"异常值： {str(outliers)}")
except Exception as e:
        print("错误：" + str(e))
    