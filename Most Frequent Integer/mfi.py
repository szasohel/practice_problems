def mfi(arr):
    dic = {}
    
    for x in arr:
        if x in dic:
            dic[x] += 1
        
        else:
            dic[x] = 1
    
    k = list(dic.keys())
    v = list(dic.values())
    
    return k[v.index(max(v))]


# test
a = [1,1,2,2,2,3,4,1,2,6]
print(mfi(a))