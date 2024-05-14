import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_genertor():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)
    FillPassword.insert(0,string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def text():
    WebsiteText = WebsiteUrl.get()
    EmailText = FillEmail.get()
    PasswordText = FillPassword.get()
    new_dict = {WebsiteText:
                    {'email':EmailText,
                     'password':PasswordText}}

    if not PasswordText or not WebsiteText:
        messagebox.showinfo(title="Oops", message="Please do not leave any fields empty")
    else:
        answer = messagebox.askyesno(title=WebsiteText, message=F"These are the details entered\n Email:{EmailText}"

                                                            F"\n Password:{PasswordText} \n Is this ok to save?")
    if answer is True:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_dict)
        except FileNotFoundError:
            with open ('data.json','w') as data_file:
                json.dump(new_dict,data_file,indent=4)
        else:
            with open ("data.json", 'w') as data_file:
                json.dump(data,data_file, indent=4)
            WebsiteUrl.delete(0,END)
            FillPassword.delete(0,END)
            FillEmail.delete(0,END)
    elif answer is False:
        WebsiteUrl.delete(0, END)
        FillPassword.delete(0, END)

# ---------------------------- SEARCH BUTTON ------------------------------- #

def search():
    website = WebsiteUrl.get()
    with open('data.json','r') as data_file:
        data = json.load(data_file)
        try:
            dictionary = data[website]
        except KeyError:
            messagebox.showinfo(title='ERROR', message="Website doesn't exist,Try Again!")
        else:
            email = dictionary['email']
            password = dictionary['password']
            messagebox.showinfo(title=website, message=f"Email:{email}\n Password:{password}")





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
canvas = Canvas(width=180, height=180)
picture = PhotoImage(file='logo.png')
canvas.create_image(90,90, image=picture)
canvas.grid(row=0, column=2,columnspan=2)
website = Label(text="Website:", font=('Arial',13))
website.grid(row=2,column=1,sticky='w')
WebsiteUrl = Entry(width=20)
WebsiteUrl.grid(row =2,column=2)
WebsiteUrl.focus()
search = Button(text='Search', width=10, command=search)
search.grid(row=2,column=3)
email = Label(text="Email/Username:", font=('Arial', 13))
email.grid(row=3, column=1, sticky='w')
FillEmail = Entry(width=36)
FillEmail.insert(END, string='agajan1197@gmail.com')
FillEmail.grid(row=3, column=2,columnspan=2)


password_label = Label(text="Password:", font=('Arial', 13))
password_label.grid(row=4, column=1,sticky='w')

FillPassword = Entry(width=21)
FillPassword.grid(row=4, column=2)

PasswordButton = Button(text="Generate Password", width=12,command=password_genertor)
PasswordButton.grid(row=4, column=3)


ADD = Button(text="Add",width=36,command=text)
ADD.grid(row=5, column=2, columnspan=2)


window.mainloop()
