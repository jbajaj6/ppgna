def sum_list(x, n):
    lst = []
    for i in range(x):
        lst.append(n)
        n -= 1
    return lst

print(sum_list(20, 1000))