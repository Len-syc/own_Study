def Fact(x:int) -> str:
    if x==1:
        return 1
    return x*Fact(x-1)