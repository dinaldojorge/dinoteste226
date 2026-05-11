import base64
import streamlit as st

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Perfil Dinaldo",
    layout="wide"
)

# FUNÇÃO BASE64
def get_base64(img_file):
    with open(img_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# FUNDO VERDE
st.markdown("""
<style>
.stApp {
    background-color: #004B2C;
}

h1, h2, h3, h4, h5, h6, p, div {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# LOGO NIKE CLICÁVEL
# ============================================================

img_nike = get_base64("NIKE.png")

st.markdown(f"""
<div style="text-align:center;">
    <a href="https://nike.com" target="_blank">
        <img src="data:image/png;base64,{img_nike}" width="300">
    </a>
</div>
""", unsafe_allow_html=True)

# ============================================================
# TÍTULO
# ============================================================

st.write("## NOME DINALDO JORGE")

# ============================================================
# FOTO + TEXTO AO LADO
# ============================================================

col1, col2 = st.columns([1,3])

with col1:
    st.image("DINO.png", width=180)

with col2:
    st.markdown("""
<div style="margin-top: 60px;">

🎓 Formado no curso TELECO  
📅 49 anos  
💻 Desenvolvedor Python e Streamlit  
🚀 Especialista em aplicativos e automações

</div>
""", unsafe_allow_html=True)

# ============================================================
# BOTÃO/IMAGEM WHATSAPP
# ============================================================

img_za = get_base64("ZA.png")

st.markdown(f"""
<div style="text-align:center; margin-top:40px;">
    <a href="https://wa.me/5583998234415" target="_blank">
        <img src="data:image/png;base64,{img_za}" width="300">
    </a>
</div>
""", unsafe_allow_html=True)
