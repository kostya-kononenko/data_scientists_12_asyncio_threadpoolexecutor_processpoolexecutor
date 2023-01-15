from time import perf_counter
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def use_process_pool_executor():
    start = perf_counter()
    with ProcessPoolExecutor() as executor:
        f1 = executor.submit(factorial, 50)
        f2 = executor.submit(factorial, 100)
        print(f1.result())
        print(f2.result())
    finish = perf_counter()
    result = finish - start
    print(f'Виконання з ProcessPoolExecutor зайняло {result} секунд')
    return result


def use_thread_pool_executor():
    start = perf_counter()
    with ThreadPoolExecutor() as executor:
        f1 = executor.submit(factorial, 50)
        f2 = executor.submit(factorial, 100)
        print(f1.result())
        print(f2.result())
    finish = perf_counter()
    result = finish-start
    print(f'Виконання з ThreadPoolExecutor зайняло {result} секунд')
    return result


def main():
    b = use_process_pool_executor()
    a = use_thread_pool_executor()
    if a < b:
        result = 'ThreadPoolExecutor бистріше'
    else:
        result = 'ProcessPoolExecutor бистріше'
    print(result)


main()
