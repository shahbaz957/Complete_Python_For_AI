from logger import logging

def add(a , b):
    logging.debug("Add function is operating ")
    return a + b

logging.debug("Add function is completed")
add(1 , 4)