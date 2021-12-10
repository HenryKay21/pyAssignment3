# Roles:
    # Creating input statements for name and withdraw amount (Henry)
    # Creating conditional statements to initiate or deny transaction (Joel)
    # Creating a statement to return a message for a successfull or failed transaction (Henry and Joel)

# Defining the function
def atmWithdraw():
    customerName = input ("Please enter your full name: ")
    customerPIN = int(input ("Please enter your PIN number: "))
    openingBal = 500000
   
    # Conditional statements
    if (customerPIN == int(1234)):
            amount = int(input("Please enter your withdraw amount: "))
            if (amount <= openingBal):
                openingBal -= amount
                print("Your account balance is now: ", openingBal,".", "Thank you for banking with us!")

    # Return messages for the conditions        
            else:
                print("Dear customer your account balance is insufficient!")

    else:
            print("Incorrect PIN. Please enter the correct PIN number!")

atmWithdraw()
 