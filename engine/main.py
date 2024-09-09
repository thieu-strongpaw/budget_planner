# Created by Thieu Strongpaw
# 9/2/2024
# A simple personal budget

import pandas as pd
import gui

def main():

    # Lists to hold the dataframes

    accounts = []
    transactions = []

    # Create dataframes to store data
    
    account_columns = ['Name', 'Type', 'Balance', 'Open Date', 'ID']
    accounts_df = pd.DataFrame(columns=account_columns)

    transactions_columns = ['ID', 'Date', 'Account', 'Amount']
    transactions_df = pd.DataFrame(columns=transactions_columns)

    print(accounts_df)
    print(transactions_df)

    gui.main_loop()

if __name__ == "__main__":
    main()
