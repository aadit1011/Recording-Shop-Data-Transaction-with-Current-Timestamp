import pandas as pd
from datetime import datetime

# Input shop name
shop = input('Enter the name of your shop: ')

def record_transaction(name, number, address, product, quantity, price, file_path='transactions.csv'):
    """
    Records a transaction by appending the details to a CSV file.
    
    Parameters:
    name (str): Customer's name
    number (int): Customer's mobile number
    address (str): Customer's address
    product (str): Product name
    quantity (int): Quantity of the product purchased
    price (float): Price per unit of the product
    file_path (str): Path to the CSV file where the transaction will be recorded. Default is 'transactions.csv'.
    """
    
    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    total = price * quantity  # Calculate total price
    
    # Create a DataFrame for the new entry
    new_entry = pd.DataFrame({
        'Name': [name],  # List with a single element to ensure correct DataFrame format
        'Mobile Number': [number],
        'Address': [address],
        'Product': [product],
        'Price': [price],
        'Quantity': [quantity],
        'Total Price': [total],
        'Timestamp': [current_time]  # Current timestamp
    })
    
    # Append the new entry to the CSV file
    new_entry.to_csv(
        file_path,  # Path to the CSV file
        mode='a',  # Append mode
        index=False,  # Do not write the index
        header=not pd.io.common.file_exists(file_path)  # Write header if file does not exist
    )

# Greeting message
print(f'Welcome To {shop}.....\nGet the Best Service')

# Input customer details and transaction information
cname = input("Enter your name: ") 
cnumber = int(input('Enter your number: ')) 
cadd = input('Enter your address: ') 
cprod = input('Enter the product name: ')
cquat = int(input('Enter the product quantity: ')) 
cprice = float(input('Enter the Price: '))

# Record the transaction
record_transaction(cname, cnumber, cadd, cprod, cquat, cprice)

# Confirmation message
print('Your details have been successfully recorded.....Thank you for buying the product.')
