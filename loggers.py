import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s',
                    datefmt='%Y-%m-%d,%H:%M:%S')





