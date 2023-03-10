import tkinter as tk
from tkinter import ttk
import base64
from PIL import Image
from bitcoinrpc.authproxy import AuthServiceProxy

# Set rpc_user and rpc_password in the litecoin.conf file
rpc_user = 'YOUR_RPC_USERNAME'
rpc_password = 'YOUR_RPC_PASSWORD'

# Connect to Bitcoin daemon
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))

# Get list of Omni Layer token properties
data = rpc_connection.omni_listproperties()

# Create a set to store the names that have already been printed
printed_names = set()

# Loop through the properties and add the property name to the set of printed names
# if the length of the data field is 255 and "JPEG" is in the name
for prop in data:  
    if len(str(prop['data'])) == 255 and "jpeg" or "JPEG" in prop['name']:
        printed_names.add(prop['name'][:-5])

# Create the GUI window
root = tk.Tk()
root.geometry("500x300")
root.title("Omni Layer Image Viewer")

# Create a dropdown menu widget
property_name = tk.StringVar(root)
property_name.set("Select Property") # default value
property_menu = ttk.OptionMenu(root, property_name, *printed_names)
property_menu.pack()

# Create a button to display the image
def display_image(data):
    # Filter list for user-defined property name and add property data to dictionary
    token_dict = {}
    for prop in data:
        if prop['name'][:-5] == property_name.get():
            num = prop['name'][-5:]
            d1 = prop['category']
            d2 = prop['subcategory']
            d3 = prop['url']
            d4 = prop['data']

            # Add property data to dictionary, handling cases where data is longer than 255 characters
            if len(d1) == 255:
                token_dict[num+'d1'] = d1
            if len(d1) >= 1 and d1[-1] == '=':
                token_dict[num+'d1'] = d1
            if len(d1) >= 2 and d1[-2] == '=':
                token_dict[num+'d1'] = d1

            if len(d2) == 255:
                token_dict[num+'d2'] = d2
            if len(d2) >= 1 and d2[-1] == '=':
                token_dict[num+'d2'] = d2
            if len(d2) >= 2 and d2[-2] == '=':
                token_dict[num+'d2'] = d2

            if len(d3) == 255:
                token_dict[num+'d3'] = d3
            if len(d3) >= 1 and d3[-1] == '=':
                token_dict[num+'d3'] = d3
            if len(d3) >= 2 and d3[-2] == '=':
                token_dict[num+'d3'] = d3

            if len(d4) == 255:
                token_dict[num+'d4'] = d4
            if len(d4) >= 1 and d4[-1] == '=':
                token_dict[num+'d4'] = d4
            if len(d4) >= 2 and d4[-2] == '=':
                token_dict[num+'d4'] = d4

    # Sort dictionary by keys and concatenate values
    sorted_token = dict(sorted(token_dict.items()))
    data = ''.join(sorted_token.values())

    # Decode base64 encoded data and write to file
    decodeit = open('out.jpeg', 'wb')
    decodeit.write(base64.b64decode(data))
    decodeit.close()

    # Open image file and display using PIL
    im = Image.open('out.jpeg')
    im.show()



display_button = tk.Button(root, text="Display Image", command=lambda: display_image(data))
display_button.pack()

# Run the GUI event loop
root.mainloop()
