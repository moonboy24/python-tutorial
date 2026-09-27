
import logging

# Config Logging
logging.basicConfig(
    level= logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',
    filemode='w'
)

def divide(a , b):
    logging.info(f"Divided {a} by {b}")
    try:
        result = a/b
        logging.debug(f"Result : {result}")
        return result
    except ZeroDivisionError:
        logging.error("Tried to divide by Zero")
        return None
    
# Test

divide(10,5)
divide(10,0)