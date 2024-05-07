# -*- coding: utf-8 -*-
"""
Created on Fry 18 Jan 2024

@author: Enrique Revuelta García
"""

import streamlit as st


st.set_page_config(layout='centered', page_icon='⚽', page_title='Fifa 23 Scouting App')

st.write("# FIFA 23 Scouting APP ⚽")

st.sidebar.success("## Menú")

st.markdown(
    """
    En el menú lateral podreas navegar por las diferentes páginas de la aplicación, en próximas iteraciones
    iremos añadiendo más páginas.
    
    ### ¿Qué contenido encontraremos en FIFA 23 Scouting APP?
    - Dashboards con las estadísticas de los jugadores incluidos en la base de datos de FiFa 23
    - Una aplicación que nos permitirá buscar posibles sustitutos a un jugador de cualquier equipo
      (hasta la fecha se devuelven los 5 perfiles más similares, ampliaremos el número en el futuro
      y se podrán añadir filtros especificos, tales como edad, coste de mercado, media, etc...)
    - Aplicación para comparar jugadores una vez que tenemos el candidato para sustituir a nuestro jugador
    
    """
)

image_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Easports_fifa_logo.svg/800px-Easports_fifa_logo.svg.png'

st.image(image_url)


