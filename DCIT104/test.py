def calAverage():
    average = 0
    numbers = []
    total = 0
    for i in range(10001):
        if i % 2 == 0:
            numbers.append(i)
        
    for i in numbers:
        total +=i
    
    average = total/len(numbers) 
    #print(total)
    #print(len(numbers))
    
    return average


print(calAverage())