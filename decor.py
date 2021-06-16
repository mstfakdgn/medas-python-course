# from functools import lru_cache
#
# @lru_cache(maxsize=3)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)
#
# print(fib(499))



# from memory_profiler import profile
#
# @profile
# def high_memory_func():
#     large_list = list(range(100000))
#     double_large_iterator = map(lambda x: x*2, large_list)
#     double_large_list = list(double_large_iterator)
#     del double_large_iterator
#     print('finished')
#
# high_memory_func()