
# file = open("filename.txt", "w")
# file.write("Welcome to Py file handling\n")
# file.write("This is write operation\n")
# file.close()

# file = open("filename.txt" , "r")
# content = file.read()
# print("File Content\n",content)
# file.close()

# file = open("filename.txt" , "a")
# file.write("Added a new line\n")
# file.close()

with open("filename.txt" , "r") as file:
    for line in file:
        print(line.strip())