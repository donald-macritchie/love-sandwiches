import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market")
    print("Data should be six numebers, sperated by commas.")
    print("Example: 10,20,30,40,50,60 \n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")


get_sales_data()


# Collect sales data from the user

# Add sales data into sales worksheet. 

# Calculate surplus numbers

# Add surplus data to surplus worksheet

# Calculate the average sales for the last 5 markets

# Add calculated stock numbers into the stock worksheet
