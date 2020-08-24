import concurrent.futures
import time

from os import listdir, path, mkdir

start = time.perf_counter()

texts = listdir('texts')
texts = [i for i in texts if i.split('.')[-1] == 'txt']

start = time.perf_counter()
# for text in texts:
def lorem_counter(text):
    f = (open('texts/'+text)).read().upper()
    w = open('texts/upper'+text, 'w+')
    w.write(f)

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(lorem_counter, texts)

end = time.perf_counter()
print(end-start)

