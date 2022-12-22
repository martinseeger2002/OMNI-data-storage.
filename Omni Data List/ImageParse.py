from bitcoinrpc.authproxy import AuthServiceProxy #you need to install bitcoinRPC for this to work. "pip install python-BitcoinRPC"
# import the PropertyList class from the script where it's defined
from PropertyList import PropertyList

def extract_data(properties, user_def_name, serial_num):
    result_str = ""
    for data in properties:
        if data['name'][:-5] == user_def_name and data['name'][-5:] == str(serial_num)[-5:]:
            result_str += data['category'] + data['subcategory'] + data['url'] + data['data']
            if "=" in result_str:
                return result_str
    serial_num += 1
    return extract_data(properties, user_def_name, serial_num)

# create an instance of the PropertyList class
property_list = PropertyList('YOUR_RPC_USERNAME', 'YOUR_RPC_PASSWORD')

# call the get_properties method on the instance
properties = property_list.get_properties()
print(properties)

rpc_user = 'YOUR_RPC_USERNAME'
rpc_password = 'YOUR_RPC_PASSWORD'
user_def_name = input('Enter prop name try')
serial_num = 100001

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))
data = rpc_connection.omni_listproperties()

result = extract_data(properties, user_def_name, serial_num)
print(result)
