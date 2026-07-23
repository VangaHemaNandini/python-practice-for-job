username = "Ekanshuu"
password = "Shiva@143"
if username == "Ekanshuu":
    if password == "Shiva@143":
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Incorrect username")    
# program 2
pin = "1234"
balance = 5000
if pin == "1234":
    if balance == 5000:
        print("Transaction successful")
    else:
        print("Insufficient balance")
else:
    print("Incorrect pin")
# program 3
age = int(input("Enter your age: "))
has_ticket = True 
if age >= 18:
    if has_ticket:
        print("Enjoy the movie")
    else:
        print("by the ticket first")
if age < 18:
    print("You are not allowed to watch the movie")      
# program 4
amount = int(input("Enter the amount: "))
is_member = True
if amount >= 3000:
    if is_member:
        print("You get a 20% discount")
    else:
        print("You get a 10% discount")
        print("No discount available")
# program 5
salary = int(input("Enter your salary: "))
employee_has_worked = int(input("Enter years of experience: "))
if salary >= 50000:
    if employee_has_worked >= 5:
        print("bonus is 10000")
    else:
        print("bonus is 5000")
else:        
        print("No bonus ")                                 




              