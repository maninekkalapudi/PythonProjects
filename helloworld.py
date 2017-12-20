print("Hello World!")

a = 100
print (a)

def printFunction(a):
    
    print("print function value: ",a)

def sum(start, end):
    if(start>end):
        print("Start should be lesser than end")
        return
    result = 0
    for i in range(start, end+1):
        result += i
    return result
 
sumresult = sum(10, 50)
printFunction(sumresult)
