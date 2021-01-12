a = input("Enter smething : ")
if a.find("  "):
    a = a.replace("  ", " ")
    print("The output is : ", a)
else:
    print("Can't find any double spaces")