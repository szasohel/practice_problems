def find_pair(arr):
    dic = {}
    
    for x in arr:
        if x in dic:
            return dic[x],x
        else:
            dic[10 - x] = x
    

# test
a = [2 , 3 , 4 , 5, 8]
print(find_pair(a))