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

data_properties = property_list.get_properties()
print(data_properties)
print ("")
num_of_props = (len(properties)-1)
print(num_of_props)
user_def_name = input('Enter prop name try')
result_str = ""





def extract_data(result_str,):
    prop_num = 0
    serial_nums = []
    while prop_num < num_of_props:
        if properties[prop_num]['name'][:-5] == user_def_name and (properties[prop_num]['name'][-5:]) not in serial_nums:
            serial_nums.append(properties[prop_num]['name'][-5:])
        prop_num += 1
        print((serial_nums))
    if prop_num == num_of_props:
        prop_num = 0
        print((serial_nums))



extract_data(result_str, serial_num)

