import threading
import time
import timeit
#
# def print_time(count_max, delay=1):
#     count = 0
#     while count < count_max:
#         count += 1
#         print(threading.current_thread(), time.strftime('%H:%M:%S', time.localtime()))
#         time.sleep(delay)
#
#
# t = threading.Thread(target=print_time, args=(2,))
# t_ = threading.Thread(target=print_time, args=(4,))
#
# t.start()
# t_.start()
#
# print(t.name, t.is_alive())
# print(t_.name, t_.is_alive())
#
# t.join()
# t_.join()
#
# print(t.name, t.is_alive())
# print(t_.name, t_.is_alive())
import threading

# a = 0
#
# def fnc():
#     global a
#     for _ in range(400000):
#         a += 1
#
# thread_list = []
#
# for _ in range(10):
#     t = threading.Thread(target=fnc)
#     t.start()
#     thread_list.append(t)
#
# for t in thread_list:
#     t.join()
#
#
# print(a)
#
# # t1        t2
# # 0 -> 1    0 -> 1
# # -         1 -> 2
# # 2 -> 3    2 -> 3
#
# #Bütün thretler global değişkene ulaşabilir.



# a = 0
#
# thread_lock = threading.Lock()
# def bad_performance_lock():
#     global a
#     a = 0
#     def fnc():
#         global a
#         for _ in range(400000):
#             thread_lock.acquire()
#             a += 1
#             thread_lock.release()
#
#     thread_list = []
#
#     for _ in range(10):
#         t = threading.Thread(target=fnc)
#         t.start()
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.join()
#     print(a)
#
# print(timeit.timeit(bad_performance_lock, number=3))




# a = 0
#
# thread_lock = threading.Lock()
# def high_performance_lock():
#     global a
#     a = 0
#     def fnc():
#         global a
#         thread_lock.acquire()
#         for _ in range(400000):
#             a += 1
#         thread_lock.release()
#
#     thread_list = []
#
#     for _ in range(10):
#         t = threading.Thread(target=fnc)
#         t.start()
#         thread_list.append(t)
#
#     for t in thread_list:
#         t.join()
#     print(a)
#
# print(timeit.timeit(high_performance_lock, number=3))



# #Process
# import multiprocessing
# import time
#
# def print_time(count_max, delay=1):
#     count = 0
#     while count < count_max:
#         count += 1
#         print(multiprocessing.current_process, time.strftime('%H:%M:%S', time.localtime()))
#         time.sleep(delay)
#
# if __name__ == '__main__':
#     print(multiprocessing.cpu_count())
#     t = multiprocessing.Process(target=print_time, args=(2,))
#     t_ = multiprocessing.Process(target=print_time, args=(4,))
#
#     t.start()
#     t_.start()
#
#     print(t.name, t.is_alive())
#     print(t_.name, t_.is_alive())
#
#     t.join()
#     t_.join()
#
#     print(t.name, t.is_alive())
#     print(t_.name, t_.is_alive())


from multiprocessing import Pool, current_process, cpu_count
from math import sqrt

def is_price(number):
    if number < 2:
        raise ValueError
    if number ==2:
        return True
    if number % 2 == 0:
        return False

    divisions = range(3, int(sqrt(number)), 2)

    for d in divisions:
        if number % d == 0:
            return False

    return  True

def prime_check(numbers):
    return {"process name:": current_process().name, 'data:': sum(n for n in numbers if is_price(n))}


if __name__ == '__main__':
    ranges = [ range(2, 500000), range(500000, 1000000), range(1000000, 1500000), range(1500000, 2000000)]
    p = Pool(processes=cpu_count()-1)
    result = p.map_async(prime_check, ranges).get()
    print(result)
    p.close()
