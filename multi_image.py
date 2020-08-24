import time
import concurrent.futures
from PIL import Image, ImageFilter
from os import listdir, path, mkdir

# dosyadaki imageleri açıp birkaç işlemden geçirip
# işlenen imageleri yeni bir dosya içerisine yazıyorum.
# multiprocessing olmadan 25 sn sürüyor.
# multiprocessing ile 11 sn sürüyor.

img_names = listdir('images')
img_names = [i for i in img_names if i.split('.')[-1] == 'jpg']

start = time.perf_counter()

size = (1200, 1200)

if not path.isdir('processed'):
    mkdir('processed')

def process_image(image_name):
    img = Image.open("images/" + image_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{image_name}')
    print(f'{image_name} was processed')

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(process_image, img_names)

end = time.perf_counter()

print(end-start)
