import re

from datetime import datetime

def input_mandatory(msg):
    while True:
        user_input = input(msg)
        if user_input == "":
            print("❗ This field cannot be empty, try again!!!")
        else:
            return user_input

def date_input_mandatory(msg):
    while True:
        user_input = input(msg + " (DD-MM-YYYY): ")
        try:
            # Try to parse the date to check if it's valid
            date_obj = datetime.strptime(user_input, "%d-%m-%Y")
            # Reformat to ensure leading zeros and consistent format
            formatted_date = date_obj.strftime("%d-%m-%Y")
            return formatted_date
        except ValueError:
            print("❌ Invalid date. Please enter a valid date in DD-MM-YYYY format.")

def date_input(msg):
    while True:
        user_input = input(msg + " (DD-MM-YYYY): ")
        try:
            # Since this isn't mandatory, if the user_input is empty we return and do not check the date
            if user_input == "":
                return user_input
            # Try to parse the date to check if it's valid
            date_obj = datetime.strptime(user_input, "%d-%m-%Y")
            # Reformat to ensure leading zeros and consistent format
            formatted_date = date_obj.strftime("%d-%m-%Y")
            return formatted_date
        except ValueError:
            print("❌ Invalid date. Please enter a valid date in DD-MM-YYYY format.")

def number_input(msg):
    while True:
        user_input = input(msg + " (10-digit phone number): ")
        # Since this isn't mandatory, if the user_input is empty we return and do not check the phone number
        if user_input == "":
                return user_input
        elif user_input.isdigit() and len(user_input) == 10:
            return user_input
        else:
            print("❌ Invalid phone number. Please enter exactly 10 digits.")

def email_input(msg):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    while True:
        user_input = input(msg + " (e.g., firstname.surname@email.com): ")
        if user_input == "":
            return user_input
        if re.match(pattern, user_input):
            return user_input
        else:
            print("❌ Invalid email. Please enter a valid email address.")

def address_input(msg):
    # Pattern: Number + Street Name + ', ' + City
    pattern = r'^\d+\s+[A-Za-z\s]+,\s*[A-Za-z\s]+$'
    
    while True:
        user_input = input(msg + " (e.g., 71 Dalton Street, Manchester): ")
        if user_input == "":
            return user_input
        if re.match(pattern, user_input):
            return user_input
        else:
            print("❌ Invalid address. Please use the format: 'Number Street Name, City'")           
            
def amount_input_mandatory(msg):
    while True:
        try:
            amount = float(input(msg))
            if amount <= 0:
                print("❗ The monetary amount must be greater than zero.")
            else: 
                return amount
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

def confirmation_input(msg):
    while True:
        user_input = input(msg + " (Y / N): ").lower()
        if user_input == "":
            print("Enter Y or N, please try again.")
        elif user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print("❌ Invalid input. Please enter a Y or N.")
