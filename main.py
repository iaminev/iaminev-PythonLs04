from random import randint


def create_array(objs: int):
    return [randint(1, 9) for _ in range(objs)]

def task22():
    n = int(input("введите n :"))
    array_n = create_array(n)
    m = int(input("введите m :"))
    array_m = create_array(m)
    print(array_n)
    print(array_m)
    array_new = sorted(set(array_n).intersection(array_m))
    print(array_new)


def task24():

    print('task 24')

if __name__ == '__main__':
    task22()
    task24()
