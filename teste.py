import base64
import streamlit as st

#------------------------------------------------------------
def get_base64(img_file):
    with open(img_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64("NIKE.png")

st.markdown(f"""
<div style="text-align:center;">
    <a href="https://nike.com" target="_blank">
        <img src="data:image/png;base64,{img}" width="300">
    </a>
</div>
""", unsafe_allow_html=True)

#---------------------------------------------------------------


#st.image("NIKE.png")
st.write("NOME DINALDO JORGE")
st.image("DINO.png")
st.write("DINALDO 49 ANOS FORMADO NO CURSO TELECO")
st.image("ZA.png")
st.link_button("Acessar", "https://wa.me/558399823445")
