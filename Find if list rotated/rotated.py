def is_rotated(a,b):
    ind = a.index(b[0])
    length = len(a)-ind
    
    if len(a) != len(b):
        return False
    else:
        for x in range(0,length):
            if b[x] != a[x+ind]:
                return False                
        for y in range(length, len(a)):
            if b[y] != a[y-length]:
                return False
        else:
            return True
    
    
        

# test
print("Test 1 with arrays b = [1,2,3,4,5,6,7,8,9]" 
      + "a = [5,6,7,8,9,1,2,3,4]")
b = [1,2,3,4,5,6,7,8,9]
a = [5,6,7,8,9,1,2,3,4]
print ("Result:", is_rotated(a,b))

print("Test 2 with arrays a = [1,2,3,4,5,6,7,8,9]" 
      + "b = [5,6,7,8,9,1,2,3,4]")

a = [1,2,3,4,5,6,7,8,9]
b = [5,6,7,8,9,1,2,3,4]

print ("Result:", is_rotated(a,b))

print("Test 3 with arrays a = [1,2,3,4,5,6,7,7,9]" 
      + "b = [5,6,7,8,9,1,2,3,4]")

a = [1,2,3,4,5,6,7,7,9]
b = [5,6,7,8,9,1,2,3,4]

print ("Result:", is_rotated(a,b))

            