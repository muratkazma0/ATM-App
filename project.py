balance = 1000  

def check_balance():
    print(f"Your balance : {balance} TL")

def deposit(amount):
    global balance
    balance += amount                                                    
    print(f"{amount} TL deposited. Your new balance : {balance} TL") 

def withdraw(amount):   
    global balance
    if balance >= amount:
        balance -= amount
        print(f"{amount} TL withdrawn. Your new balance : {balance} TL")                                           
    else:
        print("Insufficient balance!")   

while True:
    print("Welcome to the ATM!")
    print("1 - Check Balance")
    print("2 - Deposit Money")
    print("3 - Withdraw Money")
    print("4 - Exit")

    choice = input("Please choose the operation you want to perform : ")

    if choice == '1':
        check_balance()
        
    elif choice == '2':
        amount = float(input("Enter the amount you want to deposit : "))
        deposit(amount)
        
    elif choice == '3':
        amount = float(input("Enter the amount you want to withdraw : "))
        withdraw(amount)
        
    elif choice == '4':
        print("Have a good day! See you again.")
        break
    
    else:
        print("You made an invalid choice. Please try again.")
