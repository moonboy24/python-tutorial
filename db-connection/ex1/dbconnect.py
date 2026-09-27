
import pymysql

# Step 1: Connect MySql 
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='asha12345',
    database='pytest',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:
        
        # Step2 : Create a table
        
        create_query = """
        CREATE TABLE IF NOT EXISTS employees(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(50)
        )
        """
        cursor.execute(create_query)
        
        # Step3 : Insert Query
        
        insert_query = "INSERT INTO employees (name , department) VALUES (%s , %s)"
        values = [("John" , "IT"), ("Bill" , "AI")]
        cursor.executemany(insert_query, values)
        connection.commit()
        
        # Step4: Select query
        
        select_query = "SELECT * FROM employees"
        cursor.execute(select_query)
        result = cursor.fetchall()
        

        for row in result:
            print(row)
            
            
finally:
    connection.close()