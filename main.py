from fastapi import FastAPI
from funciones import userdataa, countreviewss, genree

#countreviewss




app = FastAPI()
@app.get("/")
def root():

    return {'message': 'Bienvenido!'}



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









