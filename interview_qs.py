def evencheck(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
n = int(input("enter your range: "))
total = 0
for i in range(1,n+1):
    num = int(input("enter number {}:".format(i)))
    total = total+num
    result = evencheck(total)
    print(result)    
    