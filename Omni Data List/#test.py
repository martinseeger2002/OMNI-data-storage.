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
result_str = ""




def extract_data(result_str, serial_num):
    prop_num = 0
    serial_nums = []
    while prop_num <= num_of_props:
        if prop_num > num_of_props:
            break
        if properties[prop_num]['name'][:-5] == user_def_name:
            serial_nums.append(int(properties[prop_num]['name'][-5:]))
        prop_num += 1
    serial_nums.sort()
    print(len(serial_nums))
    for serial_num in serial_nums:
        prop_num = 0
        while prop_num <= num_of_props:
            if prop_num == num_of_props:
                prop_num = 0
            if properties[prop_num]['name'][:-5] == user_def_name and properties[prop_num]['name'][-5:] == str(serial_num).zfill(5):
                result_str += properties[prop_num]['category']
                if "=" not in result_str:
                    result_str += properties[prop_num]['subcategory']
                if "=" not in result_str:
                    result_str += properties[prop_num]['url']
                if "=" not in result_str:
                    result_str += properties[prop_num]['data']
                    break
            prop_num += 1
    return result_str
"""
def extract_data(result_str, serial_num):
    serial_nums = []
    data = {}
    
    # Collect all serial numbers for the user-defined name
    for prop in properties:
        if prop['name'][:-5] == user_def_name:
            serial_nums.append(int(prop['name'][-5:]))
    # Sort the serial numbers
    serial_nums.sort()
    
    # Extract the data for each serial number in order
    for serial_num in serial_nums:
        for prop in properties:
            if prop['name'][:-5] == user_def_name and prop['name'][-5:] == str(serial_num).zfill(5):
                data['category'] = prop['category']
                data['subcategory'] = prop['subcategory']
                data['url'] = prop['url']
                data['data'] = prop['data']
                result_str += data
                break
    
    return result_str


"""


result_str = extract_data(result_str, serial_num)
print(result_str)
