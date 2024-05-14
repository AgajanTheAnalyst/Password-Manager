from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
def set_column_weights(password_frame,columns, weight):
    for col in columns:
        password_frame.grid_columnconfigure(col, weight=weight)


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
canvas = Canvas(width=180, height=180)
picture = PhotoImage(file='logo.png')
canvas.create_image(90,90, image=picture)
canvas.grid(row=0, column=1)
website = Label(text="Website:", font=('Arial',13))
website.grid(row =5,column=0,sticky='w')
WebsiteUrl = Entry(width=35)
WebsiteUrl.grid(row =5,column=1)
email = Label(text="Email/Username:", font=('Arial', 13))
email.grid(row=6, column=0, sticky='w')
FillEmail = Entry(width=35)
FillEmail.grid(row=6, column=1)


password_frame = Frame(window)  # Create a frame to contain password entry and button
password_frame.grid(row=7, column=0, columnspan=2, sticky='w')

password_label = Label(password_frame, text="Password:", font=('Arial', 13))
password_label.grid(row=0, column=0)

FillPassword = Entry(password_frame, width=20)
FillPassword.grid(row=0, column=1, padx=(50,0))

PasswordButton = Button(password_frame, text="Generate Password", width=12)
PasswordButton.grid(row=0, column=2)
set_column_weights(window, [1, 2], 1)

ADD = Button(text="Add",width=32)
ADD.grid(row=8, column=1)


window.mainloop()
