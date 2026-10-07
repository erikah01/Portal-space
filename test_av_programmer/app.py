import streamlit as st

st.title("Mitt første nett-GUI")
navn = st.text_input("Hva liker du å spise?")
if st.button("Er det godt?"):
    st.write(f"Ja!, {navn} er godt!")

tall = st.slider("Velg et tall", 0, 100, 50)
st.write("Kvadratet er", tall**2)