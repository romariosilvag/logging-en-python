import logging

def suma(num1,num2):
    logging.warn('ejecutando suma ...')
    try:
        result = num1+num2
        logging.info(f'suma entre: {num1} y {num2}')
    except:
        logging.error('error en funcion suma: ', exc_info=True)

    return result

def resta(num1,num2):
    logging.warn('ejecutando resta ...')
    try:
        result = num1-num2
        logging.info(f'resta entre: {num1} y {num2}')
    except:
        logging.error('error en funcion resta: ', exc_info=True)

    return result

def division(num1,num2):
    logging.warn('ejecutando division ...')
    try:
        result = num1/num2
        logging.info(f'division entre: {num1} y {num2}')
    except Exception as e:
        logging.error('error en funcion division: ', exc_info=True)

    return result

def multiplicacion(num1,num2):
    logging.warn('ejecutando multiplicacion ...')
    try:
        result = num1*num2
        logging.info(f'multiplicacion entre: {num1} y {num2}')
    except:
        logging.error('error en funcion multiplicacion: ', exc_info=True)

    return result

def main():
    
    num1 = 8
    num2 = 2

    result1 = suma(int(num1),int(num2))
    result2 = resta(int(num1),int(num2))
    result3 = division(int(num1),int(num2))
    result4 = multiplicacion(int(num1),int(num2))

    print(f"Resultado suma: {result1}")
    print(f"Resultado resta: {result2}")
    print(f"Resultado division: {result3}")
    print(f"Resultado multiplicacion: {result4}")

def log():
    
    logging.basicConfig(filename='file.log', level=logging.WARNING, format='%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')


if __name__ == '__main__':
    
    log()
    main()
