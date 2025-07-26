import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

books = []
members = []
issued_books = []

if os.path.exists("data.json"):
    with open("data.json", "r") as file:
        data = json.load(file)
        books = data.get("books", [])
        members = data.get("members", [])
        issued_books = data.get("issued_books", [])

def save_data():
    with open("data.json", "w") as file:
        json.dump({"books": books, "members": members, "issued_books": issued_books}, file)

def add_book():
    title = simpledialog.askstring("Add Book", "Enter book title:")
    author = simpledialog.askstring("Add Book", "Enter author name:")
    isbn = simpledialog.askstring("Add Book", "Enter ISBN:")
    if title and author and isbn:
        books.append({"title": title, "author": author, "isbn": isbn})
        save_data()
        messagebox.showinfo("Success", f"Book '{title}' added.")

def add_member():
    name = simpledialog.askstring("Add Member", "Enter member name:")
    member_id = simpledialog.askstring("Add Member", "Enter member ID:")
    if name and member_id:
        members.append({"name": name, "id": member_id})
        save_data()
        messagebox.showinfo("Success", f"Member '{name}' added.")

def issue_book():
    member_id = simpledialog.askstring("Issue Book", "Enter member ID:")
    isbn = simpledialog.askstring("Issue Book", "Enter book ISBN:")
    if member_id and isbn:
        # Check if book exists
        for book in books:
            if book["isbn"] == isbn:
                issued_books.append({"isbn": isbn, "member_id": member_id})
                save_data()
                messagebox.showinfo("Issued", f"Book {isbn} issued to {member_id}")
                return
        messagebox.showerror("Error", "Book not found.")

def return_book():
    isbn = simpledialog.askstring("Return Book", "Enter book ISBN:")
    for record in issued_books:
        if record["isbn"] == isbn:
            issued_books.remove(record)
            save_data()
            messagebox.showinfo("Returned", f"Book {isbn} returned successfully.")
            return
    messagebox.showerror("Error", "Book not issued.")

def view_records():
    record_window = tk.Toplevel(root)
    record_window.title("All Records")
    text = tk.Text(record_window, width=60, height=25)
    text.pack()

    text.insert(tk.END, "📚 Books:\n")
    for b in books:
        text.insert(tk.END, f"{b}\n")
    text.insert(tk.END, "\n👥 Members:\n")
    for m in members:
        text.insert(tk.END, f"{m}\n")
    text.insert(tk.END, "\n📝 Issued Books:\n")
    for i in issued_books:
        text.insert(tk.END, f"{i}\n")

# --- Main Window ---
root = tk.Tk()
root.title("Library Management System")
root.geometry("400x400")

tk.Label(root, text="📘 Library Management System", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Add Book", width=30, command=add_book).pack(pady=5)
tk.Button(root, text="Add Member", width=30, command=add_member).pack(pady=5)
tk.Button(root, text="Issue Book", width=30, command=issue_book).pack(pady=5)
tk.Button(root, text="Return Book", width=30, command=return_book).pack(pady=5)
tk.Button(root, text="View All Records", width=30, command=view_records).pack(pady=5)
tk.Button(root, text="Exit", width=30, command=root.quit).pack(pady=20)

root.mainloop()
