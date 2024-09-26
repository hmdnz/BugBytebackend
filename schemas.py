from enum import Enum

from pydantic import BaseModel


class GenreURLChoices(Enum):

    ROCK = "Rock"
    REGGAE = "Reggae"
    ELECTRONIC = "Electronic"
    JAZZ = "Jazz"


# 'id': 100, 'name': 'The Kinks', 'genre': 'Rock'

class Band(BaseModel):
    id:int
    name:str
    genre:str

