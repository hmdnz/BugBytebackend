from fastapi import FastAPI, HTTPException

app = FastAPI()

BANDS = [{'id': 100, 'name': 'The Kinks', 'genre': 'Rock'}, {'id': 101, 'name': 'The Beatles', 'genre': 'Rock'}, {'id': 102, 'name': 'Pink Floyd', 'genre': 'Progressive Rock'}, {'id': 103, 'name': 'Led Zeppelin', 'genre': 'Hard Rock'}, {'id': 104, 'name': 'Queen', 'genre': 'Rock'}, {'id': 105, 'name': 'The Rolling Stones', 'genre': 'Rock'}, {'id': 106, 'name': 'Nirvana', 'genre': 'Grunge'}, {'id': 107, 'name': 'Radiohead', 'genre': 'Alternative Rock'}, {'id': 108, 'name': 'AC/DC', 'genre': 'Hard Rock'}, {'id': 109, 'name': 'Red Hot Chili Peppers', 'genre': 'Funk Rock'}, {'id': 110, 'name': 'Foo Fighters', 'genre': 'Alternative Rock'}, {'id': 111, 'name': 'The Doors', 'genre': 'Psychedelic Rock'}, {'id': 112, 'name': 'Guns N\' Roses', 'genre': 'Hard Rock'}, {'id': 113, 'name': 'The Who', 'genre': 'Rock'}, {'id': 114, 'name': 'Metallica', 'genre': 'Heavy Metal'}, {'id': 115, 'name': 'Pearl Jam', 'genre': 'Grunge'}, {'id': 116, 'name': 'Green Day', 'genre': 'Punk Rock'}, {'id': 117, 'name': 'The Clash', 'genre': 'Punk Rock'}, {'id': 118, 'name': 'Oasis', 'genre': 'Britpop'}, {'id': 119, 'name': 'The Smashing Pumpkins', 'genre': 'Alternative Rock'}, {'id': 120, 'name': 'Arctic Monkeys', 'genre': 'Indie Rock'}, {'id': 121, 'name': 'Linkin Park', 'genre': 'Nu Metal'}, {'id': 122, 'name': 'Blink-182', 'genre': 'Pop Punk'}, {'id': 123, 'name': 'Muse', 'genre': 'Alternative Rock'}, {'id': 124, 'name': 'The Cure', 'genre': 'Gothic Rock'}, {'id': 125, 'name': 'U2', 'genre': 'Rock'}, {'id': 126, 'name': 'Coldplay', 'genre': 'Alternative Rock'}, {'id': 127, 'name': 'Kings of Leon', 'genre': 'Alternative Rock'}, {'id': 128, 'name': 'The Strokes', 'genre': 'Indie Rock'}, {'id': 129, 'name': 'Imagine Dragons', 'genre': 'Pop Rock'}, {'id': 130, 'name': 'Panic! At The Disco', 'genre': 'Pop Rock'}, {'id': 131, 'name': 'The Black Keys', 'genre': 'Blues Rock'}, {'id': 132, 'name': 'Fall Out Boy', 'genre': 'Pop Punk'}, {'id': 133, 'name': 'My Chemical Romance', 'genre': 'Emo'}, {'id': 134, 'name': 'The White Stripes', 'genre': 'Garage Rock'}, {'id': 135, 'name': 'The Killers', 'genre': 'Alternative Rock'}, {'id': 136, 'name': 'Fleetwood Mac', 'genre': 'Rock'}, {'id': 137, 'name': 'The Eagles', 'genre': 'Rock'}, {'id': 138, 'name': 'Aerosmith', 'genre': 'Hard Rock'}, {'id': 139, 'name': 'KISS', 'genre': 'Hard Rock'}, {'id': 140, 'name': 'Deep Purple', 'genre': 'Hard Rock'}, {'id': 141, 'name': 'Def Leppard', 'genre': 'Hard Rock'}, {'id': 142, 'name': 'Bon Jovi', 'genre': 'Rock'}, {'id': 143, 'name': 'Journey', 'genre': 'Rock'}, {'id': 144, 'name': 'Rush', 'genre': 'Progressive Rock'}, {'id': 145, 'name': 'Alice in Chains', 'genre': 'Grunge'}, {'id': 146, 'name': 'Soundgarden', 'genre': 'Grunge'}, {'id': 147, 'name': 'R.E.M.', 'genre': 'Alternative Rock'}, {'id': 148, 'name': 'The Pixies', 'genre': 'Alternative Rock'}, {'id': 149, 'name': 'Beck', 'genre': 'Alternative Rock'}]



@app.get("/bands")
async def index() -> list [dict]:
    return BANDS


@app.get("/bands/{id}")
async def get_band_by_id(id: int) -> dict:
    for band in BANDS:
        if band['id'] == id:  # Use 'id', which is passed in from the URL
            return band
    raise HTTPException(status_code=404, detail=f"Band with id: {id} not found")
