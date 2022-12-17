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

# Filter list for user-defined property name and add property data to dictionary
user_def_name = input('Enter prop name (e.g. "monkeytest2JPEG", "charlitopanama", "SIPI_Jelly_Beans_", "monkeinnepalJPEG", "monkeytest2JPEG"):\n')
token_dict = {}
for prop in data:
    if prop['name'][:-5] == user_def_name:
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

