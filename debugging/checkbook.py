#!/usr/bin/python3
import sys

class Checkbook:
    def __init__(self):
        """
        Function Description:
        Initializes a new Checkbook instance with a balance of 0.0.
        
        Parameters:
        None
        
        Returns:
        None
        """
        self.balance = 0.0  # Set the initial balance to 0.0

    def deposit(self, amount):
        """
        Function Description:
        Deposits a specified amount into the account and updates the balance.
        
        Parameters:
        amount (float): The amount to be deposited into the account.
        
        Returns:
        None
        """
        self.balance += amount  # Add the deposit amount to the balance
        print("Deposited ${:.2f}".format(amount))  # Display the amount deposited
        print("Current Balance: ${:.2f}".format(self.balance))  # Display the updated balance

    def withdraw(self, amount):
        """
        Function Description:
        Withdraws a specified amount from the account if sufficient funds are available.
        
        Parameters:
        amount (float): The amount to be withdrawn from the account.
        
        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")  # If withdrawal exceeds balance
        else:
            self.balance -= amount  # Subtract the withdrawal amount from the balance
            print("Withdrew ${:.2f}".format(amount))  # Display the amount withdrawn
            print("Current Balance: ${:.2f}".format(self.balance))  # Display the updated balance

    def get_balance(self):
        """
        Function Description:
        Displays the current balance of the account.
        
        Parameters:
        None
        
        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))  # Print the current balance

def main():
    """
    Function Description:
    Main function to interact with the user. It allows the user to perform deposit, 
    withdrawal, and balance check actions on the Checkbook instance.
    
    Parameters:
    None
    
    Returns:
    None
    """
    cb = Checkbook()  # Create an instance of the Checkbook class
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break  # Exit the loop and end the program
        elif action.lower() == 'deposit':
            while True:
                try:
                    amount = float(input("Enter the amount to deposit: $"))  # Get deposit amount
                    if amount < 0:
                        print("Amount must be positive. Please try again.")  # Handle negative amounts
                    else:
                        cb.deposit(amount)  # Call deposit method if input is valid
                        break  # Exit the loop once the deposit is successful
                except ValueError:
                    print("Invalid input. Please enter a valid number.")  # Handle non-numeric inputs
        elif action.lower() == 'withdraw':
            while True:
                try:
                    amount = float(input("Enter the amount to withdraw: $"))  # Get withdrawal amount
                    if amount < 0:
                        print("Amount must be positive. Please try again.")  # Handle negative amounts
                    else:
                        cb.withdraw(amount)  # Call withdraw method if input is valid
                        break  # Exit the loop once the withdrawal is successful
                except ValueError:
                    print("Invalid input. Please enter a valid number.")  # Handle non-numeric inputs
        elif action.lower() == 'balance':
            cb.get_balance()  # Call get_balance method to show the current balance
        else:
            print("Invalid command. Please try again.")  # Handle invalid commands

if __name__ == "__main__":
    """
    Function Description:
    Entry point of the program. Starts the main function to interact with the user.
    
    Parameters:
    None
    
    Returns:
    None
    """
    main()  # Run the main function
