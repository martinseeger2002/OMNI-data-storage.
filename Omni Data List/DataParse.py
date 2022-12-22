from bitcoinrpc.authproxy import AuthServiceProxy #you need to install bitcoinRPC for this to work. "pip install python-BitcoinRPC"
# import the PropertyList class from the script where it's defined
from PropertyList import PropertyList

# create an instance of the PropertyList class
property_list = PropertyList('YOUR_RPC_USERNAME', 'YOUR_RPC_PASSWORD')

# call the get_properties method on the instance
rpc_user = 'YOUR_RPC_USERNAME'
rpc_password = 'YOUR_RPC_PASSWORD'
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))
properties = rpc_connection.omni_listproperties()

dataproperties = property_list.get_properties()
print(dataproperties)
print ("")

num_of_props = (len(properties))-1
print(num_of_props)
user_def_name = input('Enter prop name try')
serial_num = 1
result_dict = {}

def extract_data(result_dict):
    for prop in properties:
            name, category, subcategory, url, data = prop['name'], prop['category'], prop['subcategory'], prop['url'], prop['data']
            if name[:-5] == user_def_name:
            
                key = int(name[-5:])
             
                result_dict[key] = (category, subcategory, url, data)
                

extract_data(result_dict)


# Sort the dictionary by key
sorted_result_dict = sorted(result_dict.items(), key=lambda x: x[0])

combined_strings = []
for item in sorted_result_dict:
    combined_string = ''.join(item[1])
    combined_strings.append(combined_string)

base64_data = ''.join(combined_strings)

print(base64_data)  # Output: 'WgAAQQAAEYAA'


