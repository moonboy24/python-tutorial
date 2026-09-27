
names_list1 = {'mauvika' , 'citlali' , 'raiden'}
names_list2 = {'mauvika' , 'skirk' , 'fischl'}

# Set operation which removes the duplicates 
unique_names = set(names_list1)
print(unique_names)

# Union 
print(names_list1.union(names_list2))

# Intersection gives the same values in the both sets
print(names_list1.intersection(names_list2))

# Differences gives what the other list doesn't have
print(names_list1.difference(names_list2))
print(names_list2.difference(names_list1))

# Add
names_list1.add('Yae Miko')
print(names_list1)

# Remove
names_list1.remove('mauvika')
print(names_list1)