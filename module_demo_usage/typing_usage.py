
from typing import Union
from typing import Optional

def demoTypingOne(x : Union[int, float]=100):
    if isinstance(x, int): 
        print(f"{x} is int")
    elif isinstance(x, float): 
        print(f"{x} is float")

def demoTypeOr(y: int|float = 200):
    if isinstance(y, int): 
        print(f"{y} is int")
    elif isinstance(y, float): 
        print(f"{y} is float")

def demoTypeOption(z: Optional[int]):
    if isinstance(z, float): 
        print(z)
    elif isinstance(z, int):
        print(z)

if __name__ == "__main__":
    #  typing 对类型提示的支持 
    demoTypingOne(1)
    demoTypingOne(1.1)
    demoTypingOne()
    # 
    demoTypeOr()
    demoTypeOr(1.123)
    # 
    demoTypeOption(1)