name = input("Enter your name : ")
date = input("Enter the date : ")
time = input("Enter the time : ")
date = int(date)
time = int(time)
letter = f'''Dear |{name}|,
     You are selected!
     date : |{date}|
     Time : |{time}|'''
print(letter)

