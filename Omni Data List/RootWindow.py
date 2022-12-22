# import the PropertyList class from the script where it's defined
from PropertyList import PropertyList

# create an instance of the PropertyList class
property_list = PropertyList('YOUR_RPC_USERNAME', 'YOUR_RPC_PASSWORD')

# call the get_properties method on the instance
properties = property_list.get_properties()
print(properties)
