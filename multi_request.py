import concurrent.futures
import time
import pandas as pd
from os import path, mkdir
import requests

# örnek bir api kullandım. kelimeye göre şarkı aratıyorum. çıkan sonuçları csv'ye yazıyorum.
# 100 kelime için 40 saniye sürüyor multiprocessing olmadan
# 8 saniye sürüyor multiproccessing ile.

start = time.perf_counter()

letters = open('letters.txt').read().split(',')

if not path.isdir('songs'):
    mkdir('songs')


def search_song(letter):
    response = requests.get('https://searchly.asuarez.dev/api/v1/song/search', params={'query': letter})
    pd.DataFrame(response.json()['response']['results']
                 ).to_csv('songs/'+letter+'.csv', index=False)


with concurrent.futures.ProcessPoolExecutor() as exe:
    exe.map(search_song, letters)

end = time.perf_counter()

print(end-start)
