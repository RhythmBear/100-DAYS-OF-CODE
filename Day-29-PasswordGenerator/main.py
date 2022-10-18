from tkinter import *
from tkinter import messagebox
from password_gen import create_password
import json

FONT = ("Arial", 11)

# ----------------------------- DEFINING THE SEARCH FUNCTION--------------------------- #


def find_password():
    website = website_entry.get().title()

    if len(website) == 0:
        messagebox.showwarning(title="Oops!", message="Please don't leave the field empty")

    else:
        try:
            with open("Saved_Password.json") as database:
                data = json.load(database)

        except FileNotFoundError:
            messagebox.showwarning(title="Oooppss", message="The Database is missing")

        else:
            if website in data:
                email = data[website]['Email']
                password = data[website]['Password']
                print(f" Your Email is {email} and your password is {password}")
                messagebox.showinfo(website, message=f"Email: {email} \nPassword: {password} ")

            else:
                messagebox.showwarning(title="ERROR!", message=f"No details for {website} exists")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    print("Password generated successfully")
    gen_password = create_password()
    password_entry.delete(0, END)
    password_entry.insert(0, gen_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # Get the entries from the UI and save them to variables
    website = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()

    # Check to make sure none of the fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty")

    # Create a dialog box that confirms their details before saving it
    else:
        is_okay = messagebox.askokcancel(title="Confirm Details", message=f"These are your details for {website}: "
                                                                          f"\nEmail: {email}"
                                                                          f"\nPassword: {password} \nAre you sure? ")

    # Create new data format for the new data
        if is_okay:
            new_data = {
                            website: {
                                "Email": email,
                                "Password": password
                             }
                        }

            # Save the details into a json file format and try to catch an exception, incase it does not find the
            # specific file
            try:
                with open("Saved_Password.json", 'r') as new_file:
                    # Reading the data
                    file_to_update = json.load(new_file)
            except FileNotFoundError:
                with open("Saved_Password.json", 'w') as new_file:
                    # Creating the data from scratch if it does not exist
                    json.dump(new_data, new_file, indent=4)
            else:
                file_to_update.update(new_data)
                with open("Saved_Password.json", 'w') as file:
                    json.dump(file_to_update, file, indent=4)

            # Delete the entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)

            messagebox.showinfo(title=website, message=f" Added succesfully")


# ---------------------------- UI SETUP ------------------------------- #
# set up the logo
my_window = Tk()
my_window.title("Password Manager")
my_window.config(padx=50, pady=50)

my_canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
my_canvas.create_image(100, 100, image=image)
my_canvas.grid(column=1, row=0)

# Set up the Website label and entry
website_label = Label(text="Website :", font=FONT)
website_label.grid(row=1, column=0)

website_entry = Entry(width=35, font=FONT)
website_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=2, pady=3)
website_entry.focus()

# Set up the Usernmae label and entry
# Username Label
username_label = Label(text="Email/Username :", font=FONT)
username_label.grid(row=2, column=0)

# Username Entry
username_entry = Entry(width=50, font=FONT)
username_entry.grid(row=2, column=1, columnspan=2, sticky="w", padx=2, pady=3)
username_entry.insert(0, "femiemmanuel1990@gmail.com")

# Set up the password label and entry
password_label = Label(text="Password :", font=FONT)
password_label.grid(row=3, column=0, padx=2, pady=3)

password_entry = Entry(width=35, font=FONT)
password_entry.grid(row=3, column=1, sticky="w", padx=2, pady=3)
# Generate password button
password_button = Button(text="Generate Password", font=("Arial", 8), width=16, command=generate_password)
password_button.grid(row=3, column=2, sticky="e", pady=2, padx=2)

# Generate add button
add_button = Button(text="Add", font=("Arial", 8), width=66, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w", pady=3, padx=2)

# Create the search Button
search_button = Button(text="Search", font=("Arial", 8), width=16, command=find_password)
search_button.grid(row=1, column=2, sticky="e", pady=2, padx=2)

my_window = mainloop()
