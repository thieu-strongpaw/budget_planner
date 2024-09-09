# GUI logic

import tkinter as tk
import pandas as pd
import sqlite3  # Make sure to import sqlite3

entries = []

def display_input():
    user_input = entry.get()
    label_result.config(text=f"User Input: {user_input}")

def open_new_window(title):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry("300x200")

    tk.Label(new_window, text=f"This is the {title} window", font=("Arial", 14)).pack(pady=20)

    tk.Button(new_window, text="Return to Main Page", command=new_window.destroy).pack(pady=20)

def save_transactions():
    global entries
    data = []
    for row in range(10):
        row_data = [entries[row][col].get() for col in range(4)]
        data.append(row_data)

    df = pd.DataFrame(data, columns=['Date', 'Amount', 'Category', 'Account'])  # Corrected column names
    conn = sqlite3.connect('data/data.db')
    df.to_sql('transaction_data', conn, if_exists='append', index=False)
    conn.close()
    print("Data saved to SQLite database.")

def open_transactions_window(title):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry("500x400")

    # Use grid for all widgets in the new window
    header_label = tk.Label(new_window, text=f"This is the {title} window", font=("Arial", 14))
    header_label.grid(row=0, column=0, columnspan=4, pady=10)  # Use grid instead of pack

    label_prompt = tk.Label(new_window, text="Enter a transaction amount:")
    label_prompt.grid(row=1, column=0, columnspan=4, pady=10)  # Use grid instead of pack

    # Column headers
    columns = ['Date', 'Amount', 'Category', 'Account']
    for col in range(4):
        label = tk.Label(new_window, text=columns[col], borderwidth=1, relief="solid", padx=10, pady=5)
        label.grid(row=2, column=col, padx=5, pady=5)

    global entries
    entries.clear()

    # Entry fields
    for row in range(10):
        entry_row = []
        for col in range(4):
            entry = tk.Entry(new_window, borderwidth=1, relief="solid")
            entry.grid(row=row + 3, column=col, padx=5, pady=5)  # Adjust row numbers
            entry_row.append(entry)
        entries.append(entry_row)

    # Save button
    button_submit = tk.Button(new_window, text="Save", command=save_transactions)
    button_submit.grid(row=13, column=0, columnspan=4, pady=10)

    # Return button
    button_return = tk.Button(new_window, text="Return to Main Page", command=new_window.destroy)
    button_return.grid(row=14, column=0, columnspan=4, pady=10)

def exit_app():
    root.destroy()

root = tk.Tk()

def main_loop():
    root.title("Budget Planner")
    root.geometry("300x200")

    btn_view_accounts = tk.Button(root, text="View Accounts", command=lambda: open_new_window("View Accounts"), width=20, height=2)
    btn_view_accounts.pack(pady=5)

    btn_add_transaction = tk.Button(root, text="Add Transaction", command=lambda: open_transactions_window("Add Transaction"), width=20, height=2)
    btn_add_transaction.pack(pady=5)

    btn_budget = tk.Button(root, text="Budget", command=lambda: open_new_window("Budget"), width=20, height=2)
    btn_budget.pack(pady=5)

    btn_exit = tk.Button(root, text="Exit", command=exit_app, width=10, height=1)
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_loop()

