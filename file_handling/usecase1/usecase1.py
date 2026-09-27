
# Copying the contents from input to output

# with open("usecase-input.csv", "r") as infile , open("usecase-output.csv" , "w") as outfile:
#     for line in infile:
#         print(line.strip())
#         outfile.write(line)


# Reading the input file

# with open("usecase-input.csv" , "r") as infile:
#     for line in infile:
#         print(line.strip())


# Now only reading a specific row from the file using CSV

# import csv
# with open("usecase-input.csv" , "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row["age"])
        

# Now reading a specific row or column using split and array of index

with open("usecase-input.csv" , "r") as file:
    lines = file.readlines()
    for line in lines[1:]: #Skips the header in the CSv file(name , age , etc)
        columns = line.strip().split(",")
        # columns[0] , columns[1] , columns[2]
        print(columns[2]) #age columns => columns[2]

