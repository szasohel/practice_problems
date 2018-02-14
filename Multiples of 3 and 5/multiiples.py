'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def multiples(number):
    multiple_list = []
    summation = 0
    
    count = 1
    while(count<number):
        if(count % 3 == 0):
            multiple_list.append(count)
        elif(count % 5 == 0):
            multiple_list.append(count)
        count += 1
    
    for x in multiple_list:
        summation = summation + x
        
    return summation

print(multiples(1000))