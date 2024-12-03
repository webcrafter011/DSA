def recurred(array):
    tempArr = []
    for i in array:
        if i in tempArr:
            return i
        else:
            tempArr.append(i)


def recurred2(array):
    map = {}

    for i in range(len(array)):
        if map.get(array[i]) is not None:
            return array[i]
        else:
            map[array[i]] = i
    return None


print(recurred2([1, 2, 2, 1, 5]))
