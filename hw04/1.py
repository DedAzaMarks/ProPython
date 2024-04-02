import threading
import multiprocessing
import timeit


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def thread_fibonacci(n):
    return fibonacci(n)


def process_fibonacci(n):
    return fibonacci(n)


def thread_test(n):
    threads = []
    for _ in range(10):
        t = threading.Thread(target=thread_fibonacci, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def process_test(n):
    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=process_fibonacci, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

if __name__ == '__main__':
    n = 40
    print("Время выполнения с использованием threading:", timeit.timeit("thread_test(n)", setup="from __main__ import thread_test, n", number=1))
    print("Время выполнения с использованием multiprocessing:", timeit.timeit("process_test(n)", setup="from __main__ import process_test, n", number=1))
