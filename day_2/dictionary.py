# d= {1:"Python", 2:"C"}

my_dict = {
    "name": "Harry Potter",
    "add": "UK",
    "ph": "99999999999999"
}

# print(my_dict)
# print(type(my_dict))

# print(my_dict['name'])
# print(my_dict['ph'])


# my_list = list(my_dict)
# print(my_list) # only keys

print(my_dict.keys())
print(my_dict.values())

# my_dict.clear()
# print(my_dict)

my_dict['collge'] = "BMC"
print(my_dict)

my_dict.update({'college':'BMC Bhairahawa'})
print(my_dict)



# Mutability 
# List - > Ordered , Mutable , Duplicates , Indexing
# Tuple - > Ordered , !Mutable , Duplicates , Indexing
# Set - > !Ordered , Mutable , !Duplicates , Indexing
# Dictionary - > *Ordered , Mutable , !Duplicates , Indexing

# del my_dict("name")
my_dict['name'] = None
print(my_dict)
