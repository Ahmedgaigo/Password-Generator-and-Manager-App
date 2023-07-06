from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- SAVE PASSWORD ------------------------------- #
def search():
	with open("data.json", "r") as f:
		data = json.load(f)
		website = website_entry.get()

	try:
		web = data[website]
	except KeyError:
		messagebox.showinfo(title="Oops", message="There is no info on this website in your database")
	else:
		email = web["email"]
		password = web["password"]

		messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	password_list = [choice(letters) for char in range(randint(8, 10))]
	password_list += [choice(symbols) for cha in range(randint(2, 4))]
	password_list += [choice(numbers) for ch in range(randint(2, 4))]

	shuffle(password_list)
	pass_word = "".join(password_list)
	password_entry.insert(0, pass_word)
	pyperclip.copy(pass_word)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
	website = website_entry.get()
	email = email_entry.get()
	password = password_entry.get()

	if website == "" or password == "":
		messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")

	else:
		flag = messagebox.askokcancel(title=website, message=f"These are the details to save:\nEmail: {email}\nPassword: {password}\nIs it OK to save?")

		if flag:
			new_data = {
				website: {
					"email": email,
					"password": password,
				}
			}

			try:
				with open("data.json", "r") as file:
					# reading old data
					data = json.load(file)

			except FileNotFoundError:
				with open("data.json", "w") as doc:
					json.dump(new_data, doc, indent=4)

			else:
				# updating old data with new data
				data.update(new_data)

				# saving new data to
				with open("data.json", "w") as file:
					json.dump(data, file, indent=4)

			finally:
				website_entry.delete(0, END)
				password_entry.delete(0, END)
				website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create canvas
canvas = Canvas(width=200, height=200)

# adding image to canvas
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# text entries
website_entry = Entry(width=31)
website_entry.grid(column=1, row=1)
# focus cursor on the website entry that's the first entry
website_entry.focus()

email_entry = Entry(width=50)
email_entry.insert(0, "gaigoaan@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=generate_password, width=15)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=5, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)


window.mainloop()
