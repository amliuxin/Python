# the main function of qsort
def QuickSort(num, p, r):
    if p < r:
        q = Partition(num, p, r)
        QuickSort(num, p, q - 1)
        QuickSort(num, q + 1, r)


def Partition(num, p, r):
    x = num[r]
    i = p - 1
    for j in range(p, r):
        if num[j] <= x:
            i += 1
            num[i], num[j] = num[j], num[i]
    num[i + 1], num[r] = num[r], num[i + 1]
    return i + 1


# Deal with the input data
def Gete(data):
    lst = []
    data = data.split(' ')
    for item in data:
        lst.append(int(item))
    return lst

if __name__ == '__main__':
    data = input("Please input serveral numbers:")
    num = Gete(data)
    QuickSort(num, 0, len(num) - 1)
    print(num)
