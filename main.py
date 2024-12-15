import json
from fastapi import  FastAPI, Query
from pydantic import BaseModel, Field
from enum import Enum


from storage import storage

app = FastAPI(
    description='First site'
)

class Genres(str, Enum):
    CULTURAL = 'cultural'
    ADVENTURE = 'adventure'
    BEACH = 'beach'
    ECOTOURISM = 'ecotourism'

class NewTour(BaseModel):
    tittle: str = Field(min_length=3, examples=['Tour by middle sea'])
    name_tour: str
    price: float = Field(default=100, gt=20)
    cover: str
    tags: list[Genres] = Field(default=[], max_items=2)
    description: str

@app.get('/')
def index():
    return {'status': 200}

@app.post('/api/create')
def create_tour(tour: NewTour):
    storage.create_tour(json.loads(tour.json()))
    return

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', reload=True, host='127.0.0.1', port=5000)
