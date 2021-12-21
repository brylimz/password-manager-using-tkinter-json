from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("data.txt", mode="a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white", highlightthickness=0)
canvas = Canvas(width=200, height=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img,)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1)
email_entry.insert(0, "superuser@brylimz.com")

password_entry = Entry(width=36)
password_entry.grid(column=1, row=3)


#buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)



add_button = Button(text="Add", width=30)
add_button.grid(row=4, column=1)
add_button.config(command = save)

window.mainloop()
