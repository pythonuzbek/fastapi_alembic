from fastapi import FastAPI

import models
from database import engine

app = FastAPI()


@app.on_event('startup')
async def start():
    pass
    # await models.Base.metadata.create_all(engine)


