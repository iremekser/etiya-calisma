# import multiprocessing
import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'ilk {seconds}')
    time.sleep(seconds)
    return f'son {seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results = executor.map(do_something, secs)
    for res in results:
        print(res)

# processes = []
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something)
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()

finish = time.perf_counter()

print(finish-start)
