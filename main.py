from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white", highlightthickness=0)
canvas = Canvas(width=200, height=200, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img,  )
canvas.grid(column=2, row=1)

website_label = Label(text="Website", fg="black")
website_label.grid(column=0, row=2)
website_text = Text(height=1, width=35)
website_text.grid(column=2, row=2)


email_username = Label(text="Email/Username", fg="black")
email_username.grid(column=0, row=3)

password = Label(text="Password", fg="black")
password.grid(column=0, row=4)


window.mainloop()
