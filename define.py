def odd_even(num):
    if num%2 == 0:
        return "even"
    else:
        return "odd"
a = int(input("enter a number : "))
print(odd_even(a))

def greater(num1,num2):
    if num1 > num2:
        return "first is greater"
    else:
        return "second is greater"

num = int(input("enter first number : "))
num2 = int(input("enter second number : "))
print(greater(num,num2))
 def greatest(a,b,c):