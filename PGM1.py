#Katrina Groves
#Program 1
#CIT 120
#DUE 10/22/2019
#This program allows the user to input two values and
#provides basic calculations for them.
while True:
    num1 = int(input("Enter number or 00 to quit: "))
    if num1 == 00:
            break
    else:
        num2 = int(input("Enter number: "))
        sum=num1+num2
        minus=num1-num2
        product=num1*num2
        divide=num1/num2
        mod=num1%num2
        print("The sum is",sum)
        print("The difference is",minus)
        print("The product is",product)
        print("The quotient is",divide)
        print("The remainder is",mod)
