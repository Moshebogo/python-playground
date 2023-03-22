def func_return():
    for x in range(10):
        return x
    
def func_yield():
    for x in range(10):
        yield x


def func_print():
    for x in range(10):
        print(x)

def func_append_list():
    list = []
    for x in range(10):
        list.append(x)
    return list

print(func_return())        

print(list(func_yield()))

func_print()

print(func_append_list())