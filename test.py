import time
from tqdm import tqdm

while True:
    for i in tqdm(range(10)):
        time.sleep(1)
