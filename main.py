from fastapi import FastAPI  #Path para validación de parámetros de ruta
from fastapi.responses import HTMLResponse, JSONResponse#Me sirve para enviar contenido en formato json hacia el cliente
from pydantic import BaseModel
import datetime
from utils.jwt_admin import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.title = "Fast API app"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)


Base.metadata.create_all(bind=engine)




class User(BaseModel):
   email:str
   password:str




movies = [
    {
		"id": 1,
		"title": "Avatar",
		"overview": "En un exuberante planeta llamado Pandora viven los Na'vi",
		"year": "2009",
		"rating": 7.8,
		"category": "Drama"
	},
    {
		"id": 2,
		"title": "Fast And furious",
		"overview": "An amazing cars movie",
		"year": "2002",
		"rating": 9.8,
		"category": "Acción"
	}
]


#GET METHOD:


@app.get('/', tags = ["Home"])
def message():
    return HTMLResponse("<h1> Joshua here </h1>")




