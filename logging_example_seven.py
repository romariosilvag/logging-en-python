import logging
from logging.handlers import RotatingFileHandler

def test():
    pass


def main():
    
    handler = RotatingFileHandler('myapp.log', maxBytes=1024, backupCount=3)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
    handler.setFormatter(formatter)
    logging.basicConfig(level=logging.INFO, handlers=[handler])

    logging.info('Started')
    test()
    logging.info('Finished')

if __name__ == '__main__':
    main()