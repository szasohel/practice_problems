def single(arr):
    dic = {}
    
    for x in arr:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    
    key = list(dic.keys())
    value = list(dic.values())
    if 1 in value:
        return key[value.index(1)]
    else:
        return None

# test 1
a = [1,2,3,4,1,2,3]
print(single(a))

# test 2
a = [1,2,3,4,1,2,3,4]
print(single(a))