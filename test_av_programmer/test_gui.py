
import streamlit as st

st.title("Mitt første nett-GUI")
navn = st.text_input("Hva heter du?")
if st.button("Si hei"):
    st.write(f"Hei, {navn}!")

tall = st.slider("Velg et tall", 0, 100, 50)
st.write("Kvadratet er", tall**2)