from functools import wraps
import datetime
import time


def my_logger(origianl_funtion):
    import logging
    filename = '{}.log'.format(origianl_funtion.__name__)
    logging.basicConfig(handlers=[logging.FileHandler(filename, 'a', 'utf-8')],
                        level=logging.INFO)
    
    @wraps(origianl_funtion)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        logging.info('[{}] 실행결과 args - {}, kwargs - {}'.format(timestamp, args, kwargs))
        return origianl_funtion(*args, **kwargs)
    
    return wrapper


def my_timer(original_function):
    import time

    @wraps(original_function)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수가 실행된 총 시간 : {} 초'.format(original_function.__name__, t2))
        return result
    return wrapper


@my_timer
@my_logger
def display_info(name, age):
    time.sleep(1)
    print('dispaly({}, {}) 함수가 실행됐습니다.'.format(name, age))

display_info('zoc', 35)