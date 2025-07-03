import logging

## logging settings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers= [
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArithmeticApp")  # we are creating a logger for 'Arithmetic App'

def add(a , b):
    result = a + b
    logger.debug(f"Adding {a} and {b} --> {result}")
    return result

def subtract(a , b):
    result = a - b
    logger.debug(f"Subtracting {a} and {b} --> {result}" )
    return result 

subtract(23 , 3)
add(23 , 3)

