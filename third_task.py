import time
# print('TASK_1')
# def fibonacci_seq_generator(n):
#     n1 = 0
#     n2 = 1
#     for el in range(n):
#         yield n1
#         n1, n2 = n2, n1 + n2
#
# for num in fibonacci_seq_generator(10):
#     print(num)

import time

print('TASK_2')

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time} секунд")  # Виводимо час виконання
        return result
    return wrapper

@timer_wrapper
def prime_num_getter(n):
    num = 0
    for el in range(n):
        yield num
        num += 1

n = int(input("Введіть к-сть генерацій: "))
for i in prime_num_getter(n):
    print(i, end=' ')
