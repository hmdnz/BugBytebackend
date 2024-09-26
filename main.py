from fastapi import FastAPI, HTTPException
from genre import GenreURLChoices, BANDS


app = FastAPI()

BANDS = [{'id': 100, 'name': 'The Kinks', 'genre': 'Rock'}, {'id': 101, 'name': 'The Beatles', 'genre': 'Rock'}, {'id': 104, 'name': 'Queen', 'genre': 'Rock'}, {'id': 112, 'name': 'Guns N\' Roses', 'genre': 'Hard Rock'}, {'id': 113, 'name': 'The Who', 'genre': 'Rock'}, {'id': 181, 'name': 'The Killers', 'genre': 'Rock'}, {'id': 182, 'name': 'Bob Marley and the Wailers', 'genre': 'Reggae'}, {'id': 183, 'name': 'Daft Punk', 'genre': 'Electronic'}, {'id': 184, 'name': 'Miles Davis', 'genre': 'Jazz'}, {'id': 185, 'name': 'Linkin Park', 'genre': 'Rock'}, {'id': 186, 'name': 'Toots and the Maytals', 'genre': 'Reggae'}, {'id': 187, 'name': 'Calvin Harris', 'genre': 'Electronic'}, {'id': 188, 'name': 'John Coltrane', 'genre': 'Jazz'}, {'id': 189, 'name': 'Foo Fighters', 'genre': 'Rock'}, {'id': 190, 'name': 'Peter Tosh', 'genre': 'Reggae'}, {'id': 191, 'name': 'Red Hot Chili Peppers', 'genre': 'Rock'}, {'id': 192, 'name': 'Jimmy Cliff', 'genre': 'Reggae'}, {'id': 193, 'name': 'Skrillex', 'genre': 'Electronic'}, {'id': 194, 'name': 'Ella Fitzgerald', 'genre': 'Jazz'}, {'id': 195, 'name': 'Green Day', 'genre': 'Rock'}, {'id': 196, 'name': 'Steel Pulse', 'genre': 'Reggae'}, {'id': 197, 'name': 'The Chemical Brothers', 'genre': 'Electronic'}, {'id': 198, 'name': 'Duke Ellington', 'genre': 'Jazz'}, {'id': 199, 'name': 'The Who', 'genre': 'Rock'}, {'id': 200, 'name': 'Black Uhuru', 'genre': 'Reggae'}]


@app.get("/bands")
async def index() -> list[dict]:
    return BANDS


@app.get("/bands/{id}")
async def get_band_by_id(id: int) -> dict:
    for band in BANDS:
        if band['id'] == id:  # Use 'id', which is passed in from the URL
            return band
    raise HTTPException(status_code=404, detail=f"Band with id: {id} not found")


@app.get("/genre/{genre}")
async def get_band_by_genre(genre: str, bands=None) -> list[dict]:
    matching_bands = [band for band in BANDS if band['genre'].lower() == genre.lower()]
    if not matching_bands:
        raise HTTPException(status_code=404, detail=f"Band with genre: {genre} not found")
    return matching_bands
