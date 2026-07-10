def zhuangshi(func):
    def resfunc():
        print("装饰器开始")
        func()
        print("装饰器结束")
    return resfunc

@zhuangshi
def test():
    print("test函数")

test()
