user = input("Enter the best bts song --> ")
def song(user):
    if user == 'Mic Drop' or user == 'mic drop':
        return "Mic Drop"
    else:
        return "No"

print(song(user))

def add(num1, num2):
    return num1 + num2

user1 = input("Enter first number : ")
user2 = input("Enter second number : ")
user1 = int(user1)
user2 = int(user2)
print(add(user1,user2))

def mul(num3, num4):
    return num3 * num4

user3 = input("Enter first number : ")
user4 = input("Enter second number : ")
user3 = int(user3)
user4 = int(user4)
print(mul(user3, user4))

def sub(num5, num6):
    return num5 - num6

user5 = input("Enter first number : ")
user6 = input("Enter second number : ")
user5 = int(user5)
user6 = int(user6)
print(sub(user5, user6))