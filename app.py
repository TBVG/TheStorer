import tkinter as tk
from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheet Details
SHEET_ID = '1e7K9oJr_2gXgzfY77bgUFdzjfPkKi28qsGSZdxdycPg'

# Set up credentials for Google Sheets API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('the-storer-410409-8f94fd494079.json', scope)
client = authorize(creds)

# Open sheet
sheet = client.open_by_key(SHEET_ID).sheet1

# Function to submit the form
def submit_form():
    date_time = date_time_entry.get()
    name = name_entry.get()
    age = age_entry.get()
    address = address_var.get()
    mobile_no = mobile_no_entry.get()
    came_via = came_via_var.get()
    doctor = doctor_entry.get()
    test = test_entry.get()
    mri = mri_var.get()
    ct = ct_var.get()
    usg = usg_entry.get()
    xray = xray_entry.get()
    remarks = remarks_entry.get()
    mode = mode_var.get()
    amount = amount_entry.get()

    # Append data to Google Sheet
    sheet.append_row([date_time, name, age, address, mobile_no, came_via, doctor, test, mri, ct, usg, xray, remarks, mode, amount])

    # Optionally, show a confirmation message
    confirmation_label.config(text="Form submitted successfully!")

# Create the main window
app = tk.Tk()
app.title("Data Entry Form")

# Create form elements
labels = ["Date and Time:", "Name:", "Age:", "Address:", "Mobile Number:", "Came Via:",
          "Doctor:", "Test:", "MRI:", "CT:", "USG:", "X-ray:", "Remarks:", "Mode:", "Amount:"]

for i, label_text in enumerate(labels):
    tk.Label(app, text=label_text).grid(row=i, column=0, sticky='w')

# Use Entry widget for date and time
date_time_entry = tk.Entry(app)
date_time_entry.grid(row=0, column=1)

name_entry = tk.Entry(app)
name_entry.grid(row=1, column=1)

age_entry = tk.Entry(app)
age_entry.grid(row=2, column=1)

# Dropdown for Address
address_options = ["None", "Nagpur", "Nagpur Rural", "MP", "Other places"]
address_var = tk.StringVar(app)
address_var.set(address_options[0])  # Set default value
address_dropdown = tk.OptionMenu(app, address_var, *address_options)
address_dropdown.grid(row=3, column=1)

mobile_no_entry = tk.Entry(app)
mobile_no_entry.grid(row=4, column=1)

# Dropdown for Came Via
came_via_options = ["None", "Self/Friend", "Relative", "Rakhi", "sweta", "Dr Biviji", "Refered"]
came_via_var = tk.StringVar(app)
came_via_var.set(came_via_options[0])  # Set default value
came_via_dropdown = tk.OptionMenu(app, came_via_var, *came_via_options)
came_via_dropdown.grid(row=5, column=1)

doctor_entry = tk.Entry(app)
doctor_entry.grid(row=6, column=1)

test_entry = tk.Entry(app)
test_entry.grid(row=7, column=1)

# Dropdown for MRI
mri_options = ["None", "Brain", "Brain epilepsy", "brain stroke", "brain angio", "brain veno",
               "brain contrast", "brain with scr", "C spine", "C spine with spino", "D spine", "D spine with spino",
               "DL spine", "DL spine with spino", "LS spine", "LS spine with spini", "LS spine with HIP scr", "HIP",
               "Female pelvis", "knee", "ankle", "foot", "neck", "abdomen", "MRCP", "MRI other"]
mri_var = tk.StringVar(app)
mri_var.set(mri_options[0])  # Set default value
mri_dropdown = tk.OptionMenu(app, mri_var, *mri_options)
mri_dropdown.grid(row=8, column=1)

# Dropdown for CT
ct_options = ["None", "Brain", "3D", "Neck", "Chest", "Abdomen", "Ext", "CT other"]
ct_var = tk.StringVar(app)
ct_var.set(ct_options[0])  # Set default value
ct_dropdown = tk.OptionMenu(app, ct_var, *ct_options)
ct_dropdown.grid(row=9, column=1)

usg_entry = tk.Entry(app)
usg_entry.grid(row=10, column=1)

xray_entry = tk.Entry(app)
xray_entry.grid(row=11, column=1)

remarks_entry = tk.Entry(app)
remarks_entry.grid(row=12, column=1)

# Dropdown for Mode
mode_options = ["None", "Cash", "Credit", "Online", "Combo"]
mode_var = tk.StringVar(app)
mode_var.set(mode_options[0])  # Set default value
mode_dropdown = tk.OptionMenu(app, mode_var, *mode_options)
mode_dropdown.grid(row=13, column=1)

amount_entry = tk.Entry(app)
amount_entry.grid(row=14, column=1)

# Create a label for confirmation message
confirmation_label = tk.Label(app, text="")
confirmation_label.grid(row=15, columnspan=2)

# Create submit button
submit_button = tk.Button(app, text="Submit", command=submit_form)
submit_button.grid(row=16, columnspan=2)

# Run the Tkinter event loop only if the script is executed as the main module
if __name__ == "__main__":
    app.mainloop()
