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
#----------------------------------------------------------------
st.write("NOME DINALDO JORGE")
#----------------------------------------------------------------
col1, col2 = st.columns([1,3])
with col1:
    st.image("DINO.png", width=180)
with col2:
    st.markdown("""
    ### DINALDO JORGE
    
    🎓 Formado no curso TELECO  
    📅 49 anos  
    💻 Desenvolvedor Python e Streamlit
    """)
#-------------------------------------------------------------------
#------------------------------------------------------------
def get_base64(img_file):
    with open(img_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64("ZA.png")

st.markdown(f"""
<div style="text-align:center;">
    <a href="https://wa.me/5583998234415" target="_blank">
        <img src="data:image/png;base64,{img}" width="300">
    </a>
</div>
""", unsafe_allow_html=True)
#----------------------------------------------------------------

