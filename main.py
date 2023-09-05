from fastapi import FastAPI
from funciones import userdataa, countreviewss, genree, recomendacion_juegoo

#countreviewss




app = FastAPI()
@app.get("/")
def root():

    return {'message': 'Holamundo!'}



@app.get("/userdata/{User_id}")
async def userdata( User_id : str ):
    result = userdataa(User_id)
    return result




@app.get("/countreviews/{fecha1}, {fecha2}")
async def countreviews( fecha1 : str, fecha2 : str ):
    result = countreviewss( fecha1, fecha2 )
    return result





@app.get("/genre/{genero}")
async def genre( genero : str ):
    result = genree( genero)
    return result


@app.get("/recomendacion_juego/{item_id}")
async def recomendacion_juego( item_id : int ):
    result = recomendacion_juegoo( item_id)
    return result






