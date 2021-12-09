# Roles:
    # Creating input statements for name and withdraw amount (Henry)
    # Creating conditional statements to initiate or deny transaction (Joel)
    # Creating a statement to return a message for a successfull or failed transaction (Henry and Joel)

# Defining the function
def atmWithdraw():
    customerName = input ("Please enter your full name: ")
    customerPIN = input ("Please enter your PIN number: ")
   
    # Conditional statements
    if (customerPIN == int(1234)):
            amount = input("Please enter your withdraw amount: ")

    else:
            print("Incorrect PIN. Please enter the correct PIN number!")

atmWithdraw()


    
    
    

    
    
    # Return messages 