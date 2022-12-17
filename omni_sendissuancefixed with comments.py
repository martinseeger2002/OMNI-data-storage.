import time
import ast
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the litecoin.conf file
rpc_user = 'YOUR_RPC_USERNAME'
rpc_password = 'YOUR_RPC_PASSWORD'

# Set up an AuthServiceProxy object to interact with the local Litecoin daemon
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))


##opens arguments.txt as a dict
f = open('arguments.txt', 'r')
arguments_data = f.read()

# Parse arguments_data as a dictionary
sif_dict = ast.literal_eval(arguments_data)
f.close()

# Prompt the user for the serial number of the first token to be issued
user_input = input("Enter 0 for new token series or enter the number of the last token to be succsefully created to continue series.\n:")
serial_num = int(user_input)+100001

# Calculate the number of tokens to be issued and the maximum serial number
num_of_data = (len(sif_dict.keys())-2)
sn = num_of_data//4
snf = num_of_data/4
max_serial_num = 100000+sn-1
sns = (str(snf)[-2:])

# Read in the address, name, and other information for the tokens
address = (sif_dict['address'])
name = (sif_dict['name'])
esys = int(sif_dict['esys'])
ttype = int(sif_dict['ttype'])
preid = int(sif_dict['preid'])
amount = str(sif_dict['amount'])

# Loop through each token to be issued
while serial_num <= max_serial_num:
    if serial_num <= max_serial_num-1:
        # Read in the metadata fields for the current token
        data_num = str(serial_num)[-5:]+'d1'
        d1 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d2'
        d2 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d3'
        d3 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d4'
        d4 = (sif_dict[data_num])
        
        # Call the omni_sendissuancefixed method to create and issue the token
        result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,d2,name+str(serial_num)[-5:],d3,d4,amount)
        print(result)
        
        # Increment the serial number if the call was successful
        if len(result) == 64:
            serial_num += 1
    elif serial_num == max_serial_num:
        # Read in the metadata fields for the current token
        data_num = str(serial_num)[-5:]+'d1'
        d1 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d2'
        d2 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d3'
        d3 = (sif_dict[data_num])
        data_num = str(serial_num)[-5:]+'d4'
        d4 = (sif_dict[data_num])
        
        # Call the omni_sendissuancefixed method to create and issue the token
        result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,d2,name+str(serial_num)[-5:],d3,d4,amount)
        print(result)
        
        # Break out of the loop if the call was successful
        if len(result) == 64:
            break

if sns == '75':
    serial_num = max_serial_num+1
    data_num = str(serial_num)[-5:]+'d1'
    d1 = (sif_dict[data_num])
    data_num = str(serial_num)[-5:]+'d2'
    d2 = (sif_dict[data_num])
    data_num = str(serial_num)[-5:]+'d3'
    d3 = (sif_dict[data_num])
    result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,d2,name+str(serial_num)[-5:],d3,d4,amount) #rpc_connection.omni_sendissuancefixed
    print(result)
if sns == '.5':
    serial_num = max_serial_num+1
    data_num = str(serial_num)[-5:]+'d1'
    d1 = (sif_dict[data_num])
    data_num = str(serial_num)[-5:]+'d2'
    d2 = (sif_dict[data_num])
    result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,d2,name+str(serial_num)[-5:],'','',amount)  #rpc_connection.omni_sendissuancefixed
    print(result)
if sns == '25':
    serial_num = max_serial_num+1
    data_num = str(serial_num)[-5:]+'d1'
    d1 = (sif_dict[data_num])
    result = rpc_connection.omni_sendissuancefixed(address,esys,ttype,preid,d1,'',name+str(serial_num)[-5:],'','',amount) #rpc_connection.omni_sendissuancefixed
    print(result)
