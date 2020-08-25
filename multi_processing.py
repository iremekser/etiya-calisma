from multiprocessing import Pool


def cube(number):
    return number*number*number


if __name__ == '__main__':

    numbers = range(10)
    pool = Pool()
    #map, apply, join, close
    results = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()
    
    print(results)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# from multiprocessing import Process, Value, Array, Lock
# from multiprocessing import Queue
# import time


# def sqr(numbers, que):
#     for i in numbers:
#         que.put(i*i)


# def make_negative(numbers, que):
#     for i in numbers:
#         que.put(-1*i)


# def add_value(number, lock):
#     for i in range(1000):
#         time.sleep(0.01)
#         with lock:
#             number.value += 1
#         # lock.acquire()
#         # number.value += 1
#         # lock.release()


# def add_array(numbers, lock):
#     for i in range(1000):
#         time.sleep(0.01)
#         for i in range(len(numbers)):
#             with lock:
#                 numbers[i] += 1


# if __name__ == "__main__":

#     # # ------QUEUE-----
# #     numbers = range(1, 6)
# #     q = Queue()

# #     p1 = Process(target=sqr, args=(numbers, q))
# #     p2 = Process(target=make_negative, args=(numbers, q))

# #     while not q.empty():
# #         print(q.get())

#     # lock = Lock()
#     # # -----VALUE----
#     # # shared_number = Value('i', 0)
#     # # print(shared_number.value)
#     # # p1 = Process(target=add_value, args=(shared_number,lock))
#     # # p2 = Process(target=add_value, args=(shared_number,lock))

#     # # -----ARRAY-----
#     # # shared_array = Array('d', [0.0, 100.0, 200.0])
#     # # print(shared_array[:])
#     # # p1 = Process(target=add_array, args=(shared_array, lock))
#     # # p2 = Process(target=add_array, args=(shared_array, lock))

#     # p1.start()
#     # p2.start()

#     # p1.join()
#     # p2.join()

#     # # print(shared_number.value)
#     # # print(shared_array[:])
