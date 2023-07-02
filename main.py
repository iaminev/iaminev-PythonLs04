from random import randint


def create_array(objs: int):
    return [randint(1, 9) for _ in range(objs)]

def task22():
    print("Задача 22.")
    n = int(input("Введите n: "))
    array_n = create_array(n)
    m = int(input("Введите m: "))
    array_m = create_array(m)
    print("Первый список", array_n)
    print("Второй список", array_m)
    array_new = sorted(set(array_n).intersection(array_m))
    print("Отсортированный список из совпадающих элементов",array_new)


def task24():
    print("Задача 24.")
    berries = create_array(int(input("Введите количество кустов: ")))
    print(berries)
    max_berries = berries[len(berries)-1] + berries[0] + berries[1]
    print(f'{1}({berries[len(berries)-1]}+{berries[0]}+{berries[1]}): {max_berries}', end=', ')
    for i in range(1, len(berries), 1):
        i_next = (i+1) if i < len(berries)-1 else 0
        cur_berries = berries[i-1] + berries[i] + berries[i_next]
        print(f'{i+1}({berries[i-1]}+{berries[i]}+{berries[i_next]}): {cur_berries}', end=', ')
        if (cur_berries > max_berries):
            max_berries = cur_berries
    print()
    print(f'Максимально можно собрать: {max_berries} ягод')

if __name__ == '__main__':
    task22()
    task24()
