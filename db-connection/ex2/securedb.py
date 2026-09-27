
from password_utils import get_decrypted_password
import pymysql

def connect_to_mysql():
    conn = pymysql.connect(
        host = "localhost",
        user = "root", 
        password = get_decrypted_password(),  
        database = "pytest"
    )
    
    print("MY Sql connected")
    conn.close()
    
if __name__ == "__main__":
    connect_to_mysql()