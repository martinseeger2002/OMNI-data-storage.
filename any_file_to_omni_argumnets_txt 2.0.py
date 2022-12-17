import base64
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Open a file dialog and get the selected file's path
file_path = filedialog.askopenfilename()

# Get the file extension
_, file_extension = file_path.rsplit('.', 1)

# Read the file and encode it as base64
with open(file_path, "rb") as file_to_string:
    data_b = base64.b64encode(file_to_string.read())
    file_to_string.close
    data = str(data_b)[2:]  # this removes the "b'" from the begining of the byte string

# Split the base64-encoded string into chunks of 255 characters each
n = 255
data_list = [data[index : index + n] for index in range(0, len(data), n)]

# Prompt the user for an m-address and the name of the new token
maddress = input("enter sending m-address\n:")
name = input('Enter the name of the new token.\n:') + file_extension

# Create the dictionary
sif_dict = {"address": maddress, "esys": 1, "ttype": 1, "preid": 0, "name": name, "amount": 1}

serial_num = 100001
data_num = 0
max_data_num = (len(data_list)-1)

while data_num <= max_data_num:
    serial_str = str(serial_num)[-5:]  # pads serial_num with leading zeros to make it 5 digits
    for i in range(4):
        if data_num > max_data_num:
            break
        sif_dict[serial_str + "d" + str(i+1)] = data_list[data_num]
        data_num += 1
    serial_num += 1

# Write the dictionary to a file
with open('arguments.txt', 'w+') as f:
    f.write(str(sif_dict))

print('Your file has been converted to arguments.txt use the fee calc to see what it will cost to encode.')
