from dbconnect import *

with open("employee_details.txt" , "w") as txt:
            for row in result:
                txt.write(f"{row}\n")
                print(row)