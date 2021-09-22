from typing import Optional

from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def index():
    return {'page': 'index'}


@app.get('/page/{id}')
async def page(id: int):
    return {'page': id}


@app.get('/search/')
async def search(q: Optional[str] = None):
    if q is None:
        q = 'empty'
    return {'query': q}
