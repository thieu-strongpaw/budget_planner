# GUI logic

import tkinter as tk

def open_new_window(title):
    new_window = tk.Toplevel(root)
    new_window.title(title)
    new_window.geometry("300x200")

    tk.Label(new_window, text=f"This is the {title} window", font=("Arial", 14)).pack(pady=20)

    tk.Button(new_window, text="Return to Main Page", command=new_window.destroy).pack(pady=20)

def exit_app():
    root.destroy()

root = tk.Tk()

def main():

    root.title("Budget Planner")
    root.geometry("300x200")

    btn_view_accounts = tk.Button(root, text="View Accounts", command=lambda: open_new_window("View Accounts"), width=20, height=2)
    btn_view_accounts.pack(pady=5)

    btn_add_transaction = tk.Button(root, text="Add Transaction", command=lambda: open_new_window("Add Transaction"), width=20, height=2)
    btn_add_transaction.pack(pady=5)

    btn_budget = tk.Button(root, text="Budget", command=lambda:open_new_window("Budget"), width=20, height=2)
    btn_budget.pack(pady=5)

    btn_exit = tk.Button(root, text="Exit", command=exit_app, width=10, height=1)
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
