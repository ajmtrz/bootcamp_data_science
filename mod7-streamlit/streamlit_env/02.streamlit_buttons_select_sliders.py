import streamlit as st
import numpy as np
import pandas as pd

def main():
    # Buttons
    name = "Kike"

    if st.button(label = "Summit",
                 key   = "submit1"):
        st.write(f"{name.upper()}")

    if st.button(label = "Summit",
                 key   = "submit2",
                 type  = "primary"):
        st.write(f"First Name: {name.title()}")

    # Radio Buttons
    status = st.radio(label = "What is your status?",
                      options = ("None", "Active", "Inactive"),
                      index = 0,
                      disabled = False,
                      horizontal = True,
                      )
    if status == "Active":
        st.success("You are Active.")
    elif status == "Inactive":
        st.warning("You are Inactive.")


    # CheckBox
    if st.checkbox("Show/Hide"):
        st.text("Showing Something")

    # Expander
    with st.expander(label = "DataFrame", expanded = False):
        st.write(pd.read_csv("sources/AccidentesBicicletas_2021.csv", sep = ";"))

    # SelectBox
    modulos = ["Python", "Matemáticas", "Data Science", "SQL", "ML", "Big Data", "Streamlit"]
    choice = st.selectbox("Modulo", options = modulos)
    st.write(f"Modulo: {choice}")

    # Multiple Selection
    librerias = ["numpy", "pandas", "random", "datetime", "sklearn"]
    libreria = st.multiselect(label = "Librerias",
                             options = librerias, 
                             default = librerias)
    
    df = pd.read_csv("sources/AccidentesBicicletas_2021.csv", sep = ";")
    columnas = df.columns
    cols = ['cod_distrito','fecha', 'hora', 'sexo', 'numero', 'localizacion']
    
    filter_df = st.multiselect(label = "Select Columns",
                               options = cols,
                               default = cols
                              )
    
    
    st.dataframe(df[filter_df])

    # Slider Int, Float, Date
    age = st.slider(label     = "Age",
                    min_value = 1,
                    max_value = 100,
                    value     = 50)

    # Select Slider
    #colores = ["Amarillo", "Azul", "Rojo", "Morado", "Verde"]
    colores = ['orange', 'blue', 'red', 'violet', 'green', 'gray']
    color = st.select_slider(label  = "Choose Color",
                            options = colores,
                            value = "gray")
    
    st.markdown(f"# :{color}[color]")

if __name__ == "__main__":
    main()

