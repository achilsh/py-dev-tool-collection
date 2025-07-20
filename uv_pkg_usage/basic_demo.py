
import pandas as pd

class Demo():
    def __init__(self, a):
        self.__a = a 
    def call(self, b):
        self.__a += b 
    def get(self): 
        return self.__a
    
    

def call_pandas():
    # 读取 CSV 文件
    df = pd.read_csv('data.csv')

    # 查看数据基本信息
    print('数据基本信息：')
    df.info()

    # 查看数据集行数和列数
    rows, columns = df.shape

    if rows < 1000:
        # 小数据集（行数少于1000）查看全量数据信息
        print('数据全部内容信息：')
        print(df.to_csv(sep='\t', na_rep='nan'))
    else:
        # 大数据集查看数据前几行信息
        print('数据前几行内容信息：')
        print(df.head().to_csv(sep='\t', na_rep='nan'))
    