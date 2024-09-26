# Sample data
import time

BANDS = [{'name': 'Band A', 'genre': 'Rock'}, {'name': 'Band B', 'genre': 'Jazz'}, {'name': 'Band C', 'genre': 'Rock'}]
genre = 'rock'

# Using list comprehension
start_time = time.time()
matching_bands_lc = [band for band in BANDS if band['genre'].lower() == genre.lower()]
lc_time = time.time() - start_time

# Using regular loop
start_time = time.time()
matching_bands_loop = []
for band in BANDS:
    if band['genre'].lower() == genre.lower():
        matching_bands_loop.append(band)
loop_time = time.time() - start_time

print(f"List Comprehension Time: {lc_time}")
print(f"Regular Loop Time: {loop_time}")