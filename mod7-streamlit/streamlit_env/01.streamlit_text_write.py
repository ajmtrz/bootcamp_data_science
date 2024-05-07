import streamlit as st

import numpy as np
import pandas as pd
import requests


def main():
    # Title
    st.title("Hello Streamlit App.")

    # Text
    st.text("Hello World!")
    st.text("New Line.")
    name = "Daniel"
    st.text("Prueba.")
    st.text("Valor de variable name: {}".format(name))

    # # Header
    st.header("Header1")

    # # Subheader
    st.subheader("Subheader1")

    # # Markdown
    st.markdown("# This is markdown.")

    # # Display Colored Text/Boostraps Alert
    st.success("Success.")
    st.warning("This is a WARNING.")
    st.info("Info.")
    st.error("This is an ERROR.")
    st.exception("This is an exception.")

    # .write()
    st.write("Normal Text.")
    st.write("## This is a markdown text")
    st.write("### This is an H3 title")
    st.write("#### This is an H4 title")
    st.write("##### This is an H5 title")
    st.write("###### This is an H6 title")
    st.write(1 + 2)
    
    c1,c2,c3 = st.columns([0.25,2.5,0.25])
    with c2:
        st.write("## Texto 'centrado de aquella manera'")
    #st.dataframe(dir(st))

    # # Help
    st.help(range)

    # Display Data
    df = pd.read_csv(filepath_or_buffer = "sources/AccidentesBicicletas_2021.csv", sep = ";")
    
    # Dinamic Data
    st.dataframe(df)
    # st.write(df)

    # Static Table
    # st.table(df)

    # Adding Color
    for c in df.columns:
        st.write(c, df[c].dtype)
        
    st.dataframe(df.select_dtypes(include=np.number).style.highlight_max(axis = 1, color='lightgreen'))

    # Display JSON
    endpoint = "https://api.frankfurter.app/latest"
    response = requests.get(url = endpoint)
    st.json(response.json())

    # Display Code
    code = """
        def func():
            return x**2
        """
    st.code(body = code, language = "python")
    
if __name__ == "__main__":
    main()
    