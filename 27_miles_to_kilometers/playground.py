def add(*augs):
    result = 0
    for n in augs:
        result += n
    return result


sum_num = add(1, 2, 3, 4, 5, 6)

print(sum_num)
