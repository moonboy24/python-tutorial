
travel_summary = ("Uber" , "Chennai Airport" , 250 , "Completed")

# print(travel_summary)
# print(travel_summary[1])

for item in travel_summary:
    print(item)

print("Total Len is " ,len(travel_summary))
print("Count of Completed is:" , travel_summary.count('Completed'))
print("Index of Place is:" , travel_summary.index('Chennai Airport'))