import tkinter as tk
from tkinter import messagebox


def save_password():
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

 
    if website == "" or website == "e.g. www.something.com" or \
       username == "" or username == "e.g. user@yourmail.com" or \
       password == "" or password == "e.g. password":
        messagebox.showwarning(title="Warning / Check", message="Please fill in all fields.")
    else:
        with open("passwords.txt", "a") as file:
            file.write(f"Website: {website} | Username: {username} | Password: {password}\n")
            
        entry_website.delete(0, tk.END)
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)

        entry_website.insert(0, "e.g. www.something.com") 
        entry_website.config(fg="gray")

        entry_username.insert(0, "e.g. user@yourmail.com")
        entry_username.config(fg="gray")

        entry_password.insert(0, "e.g. password")
        entry_password.config(fg="gray", show="")

        messagebox.showinfo(title="Success Super", message="Password saved!")

def toggle_password():
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="●")

def website_click(event):
    if entry_website.get() == "e.g. www.something.com":
        entry_website.delete(0, tk.END)
        entry_website.config(fg="red")

def username_click(event):
    if entry_username.get() == "e.g. user@yourmail.com":
        entry_username.delete(0, tk.END)
        entry_username.config(fg="red")

def password_click(event):
    if entry_password.get() == "e.g. password":
        entry_password.delete(0, tk.END)
        entry_password.config(fg="red", show="?")

window = tk.Tk()
window.title(" Manager of Password")
window.config(padx=20, pady=20)
window.config(bg="lightgreen")


#tk.Label(text="Website/Page:", font=("Courier", 10, "bold")).grid(row=0, column=0, sticky="e", pady=5)
#tk.Label(text="Username/Email:", font=("Courier", 10, "bold")).grid(row=1, column=0, sticky="e", pady=5)
#tk.Label(text="Password:", font=("Courier", 10, "bold")).grid(row=2, column=0, sticky="e", pady=5)

tk.Label(text="Website:", font=("Courier", 10, "bold"), bg="orange").grid(row=0, column=0, sticky="e", pady=5)
tk.Label(text="Username/Email:", font=("Courier", 10, "bold"), bg="orange").grid(row=1, column=0, sticky="e", pady=5)
tk.Label(text="Password:", font=("Courier", 10, "bold"), bg="orange").grid(row=2, column=0, sticky="e", pady=5)

entry_website = tk.Entry(width=35, bg="lightgray", fg="gray", font=("Courier", 10, "bold"))
entry_website.insert(0, "e.g. www.something.com")
entry_website.bind("<FocusIn>", website_click)
entry_website.grid(row=0, column=1)

entry_username = tk.Entry(width=35, bg="lightgray", fg="gray", font=("Courier", 10, "bold"))
entry_username.insert(0, "e.g. user@yourmail.com")
entry_username.bind("<FocusIn>", username_click)
entry_username.grid(row=1, column=1)

entry_password = tk.Entry(width=35, bg="lightgray", fg="gray", font=("Courier", 10, "bold"))
entry_password.insert(0, "e.g. password")
entry_password.bind("<FocusIn>", password_click)
entry_password.grid(row=2, column=1)

show_password_var = tk.BooleanVar()
show_checkbox = tk.Checkbutton(text="Show password", variable=show_password_var, command=toggle_password)
show_checkbox.grid(row=3, column=1, sticky="w")

save_button = tk.Button(text="Save", width=25, font=("Courier", 10, "bold"),bg="pink", command=save_password)
save_button.grid(row=4, column=1, pady=15)

window.mainloop()
