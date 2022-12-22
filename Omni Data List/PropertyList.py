import time 
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

class PropertyList:
  def __init__(self, rpc_user, rpc_password):
    self.rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))

  def get_properties(self):
    data = self.rpc_connection.omni_listproperties() 
    properties = set()
    for prop in data:
      if len(prop['category']) == 255:
        name = prop['name'][:-5]
        properties.add(name)
    return list(properties)

# Example usage
property_list = PropertyList('YOUR_RPC_USERNAME', 'YOUR_RPC_PASSWORD')
properties = property_list.get_properties()

