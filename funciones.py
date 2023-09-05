import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
#Los dataframes que deben estar disponibles para que funcionen las funciones son:

#dinero
#steamscd
#dfreviews
#respuesta3


#1 

def userdataa( User_id : str ):
    #Utiliza los dataframes dinero, steams, dfreviews preprocesados devuelve.
    dinero = pd.read_csv('dinero.csv') # tiene la suma de dinero gastado por usuario
    steams = pd.read_csv('steams.csv') # es la tabla steams
    dfreviews = pd.read_csv('dfjuntado.csv') # Desglosa la columna reviews de la tabla reviews, presenta solo las columnas que estan adentro de reviews.
    items_count = pd.read_csv('items_count.csv') # es la tabla items pero sin la columna items.
    #user_id	funny   posted  last_edited     item_id     recommend    review
    user = User_id
    

    dinerovar = dinero.loc[dinero['user_id']==user]['suma_dinero_gastado'].values[0]  #dinero gastado por el user.

    total = dfreviews.loc[dfreviews['user_id']==user]['recommend'].count()
    istrue = dfreviews.loc[(dfreviews['user_id']==user) & (dfreviews['recommend']== True)]['recommend'].count()

    porcentaje_true = istrue/total*100 #porcentaje 

    cantidad = int(items_count.loc[items_count['user_id'] == user]['items_count'][0])

    dicc_salida = {'dinero': dinerovar, 'porcentaje_true': porcentaje_true, 'cantidad': cantidad}
    return dicc_salida


#2

#countreviews('2011-11-05', '2013-09-08')
def countreviewss( fecha1, fecha2 : str ):
    #utiliza dataframes dfreviews, retorna cantidad de usuarios que hiceron reviews y porcentaje recomendacion respecto a los reviews en las fechas dadas como parámetro.
    # las fechas deben estar en formato yyyy-mm-dd

    dfreviews = pd.read_csv('dfjuntado.csv') # Desglosa la columna reviews de la tabla reviews, presenta solo las columnas que estan adentro de reviews.
    #user_id	funny   posted  last_edited     item_id     recommend    review

    if ((type(fecha1)== str) & (type(fecha2)== str)):
        if (fecha2 > fecha1):
            cantidad_user= len(pd.unique(dfreviews.loc[(dfreviews['posted']> fecha1) & (dfreviews['posted']< fecha2)]['user_id'])) # cantidad de usuarios que hicieron reviews entre las fechas dadas
            cantidad_reviews = dfreviews.loc[(dfreviews['posted']> fecha1) & (dfreviews['posted']< fecha2)]['review'].count() # cantidad de reviews
            review_positivas = dfreviews.loc[(dfreviews['posted']> fecha1) & (dfreviews['posted']< fecha2) & (dfreviews['recommend']== True)]['review'].count()
            porcentaje = review_positivas / cantidad_reviews *100 # Porcentaje positivas
            return {'cantidad_usuarios_que_comentaron' : cantidad_user, 'porcentaje_recomendacion': porcentaje}
        else:
            return {'error2': 'la fecha2 debe ser mayor a la fecha 1'}

    else:
        return {'error1': 'las variables de entrada deben ser tipo string'} 
    

#3
#genre('Simulation')
def genree( genero : str ): 
    #dado el genero, devuelve el puesto en el  ranking del genero en funcion de la cantidad de horas jugadas en funcion de playtimeforever. 
    # El dataframe utilizado para la funcion viene procesado de otro notebook pero es una convinacion de  los items y  de steams 
    respuesta3 = pd.read_csv('respuesta3.csv')
    
    respuesta3.reset_index(inplace=True)
    a = respuesta3.loc[respuesta3['genre']== genero].index.values[0] + 1
    return {'El puesto del genero es: ': a}


# Recomendación Machine Learning

def recomendacion_juegoo(juego_actual):
    print(f"Entro a recomendacion_juego: {juego_actual}")
    
    #esta funcion retorna los 5 juegos mas parecidos en funcion de la similaridad del coseno tomando en cuenta los generos (genres)
    # Ejemplode item_id 643980
    df=pd.read_csv('steamsmodels.csv')
    # Obtener el índice del juego actual
    juego_index = df.index[df['item_id'] == juego_actual].tolist()[0]

    # Extraer las características del juego actual
    juego_features = df.iloc[juego_index, 1:].values.reshape(1, -1)  # Excluye la columna de nombres

    # Extraer todas las características de los juegos
    all_features = df.iloc[:, 1:].values

    # Calcular la similitud del coseno entre el juego actual y todos los demás
    sim_scores = cosine_similarity(juego_features, all_features)

    # Obtener los índices de los juegos más similares (excluyendo el juego actual)
    top_indices = np.argsort(sim_scores[0])[::-1][1:]

    # Obtener los nombres de los juegos recomendados
    recomendaciones = df.iloc[top_indices]['item_id'].tolist()
    return recomendaciones[0:5]