import tkinter as tk
from tkinter import messagebox

redirect = "127.0.0.1"
host = "/etc/hosts"

def block():
    website = website_entry.get().strip()
    if not website:
        tk.messagebox.showwarning("Warning","Please enter a URL of website to block.")
        return
    with open(host,'r') as file:
        data = file.read()
        if website in data:
            messagebox.showinfo("Info",f"{website} is already blocked")
        else:
            file.close()
            with open(host, 'a') as file:  # Open in append mode
                file.write(f"{redirect} {website}\n")
            blocked_website.insert(tk.END, website)
            messagebox.showinfo("Success:",f"{website} is successfully blocked.")

def unblock():
    website = website_entry.get().strip()
    if not website:
        messagebox.showwarning("Warning", "Please select a website to unblock.")
        return
    with open(host,"r") as file:
        data = file.readlines()
        file.seek(0) # Cursor at begining of file
        file.close()
    file = open(host,'w')
    for line in data:
        if website not in line:
            file.write(line)
    file.truncate()
    blocked_website.delete(tk.ACTIVE)
    messagebox.showinfo("Success:",f"{website} is successfully unblocked.")

def load_blocked():
    blocked_website.delete(0,tk.END)
    with open(host, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith(redirect):
                website = line.split()[1]
                blocked_website.insert(tk.END, website)


root = tk.Tk()
root.title("Website Blocker")

#Pack geometry

# root.geometry('400x300')

# tk.Label(root, text="Enter website URL to block:").pack(pady=5)
# website_entry = tk.Entry(root, width=40)
# website_entry.pack(pady=5)

# Buttons for blocking and unblocking websites
# block_button = tk.Button(root, text="Block Website", command=block_website)
# block_button.pack(pady=5)

# unblock_button = tk.Button(root, text="Unblock Selected Website", command=unblock_website)
# unblock_button.pack(pady=5)

# Listbox to show blocked websites
# tk.Label(root, text="Blocked Websites:").pack(pady=5)
# blocked_listbox = tk.Listbox(root, width=40, height=10)
# blocked_listbox.pack(pady=5)

# tk.Label(root, text="Enter website URL to block:").pack(pady=5)
# website_entry = tk.Entry(root, width=40)
# website_entry.pack(pady=5)

tk.Label(root, text="Enter website URL to block:").grid(row=0, column=0, padx=5, pady=5)
website_entry = tk.Entry(root, width=40)
website_entry.grid(row=0, column=1, padx=5, pady=5)

block_button = tk.Button(root, text="Block", command=block,cursor="hand2")
block_button.grid(row=1, column=0, padx=5, pady=5)
block_button.place(x = 230, y = 45)

unblock_button = tk.Button(root, text="Unblock", command=unblock,cursor="hand2")
unblock_button.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root,text="Blocked Websites:",cursor="hand2").grid(row=2, column=0, columnspan=2, pady=5)
blocked_website = tk.Listbox(root,width=40,height=10,cursor="hand2")
blocked_website.grid(row=3, column=0, columnspan=2, padx=5, pady=5)


load_blocked()

root.mainloop()