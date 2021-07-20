""" Add progress bar into loop for with tqdm module."""

# pip install tqdm

from tqdm import tqdm
from time import sleep

for i in tqdm(range(10)):
    sleep(0.2)
