import streamlit as st

# Configuración de la pestaña
st.set_page_config(page_title="Feliz Cumpleaños", page_icon="🌻")

# --- ESTILO CSS PARA FONDO OSCURO ---
st.markdown("""
    <style>
    /* Fondo oscuro con un ligero degradado para que no sea plano */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle, #1a1a1a 0%, #000000 100%);
    }

    /* Estilo del Girasol animado */
    .girasol {
        font-size: 100px;
        text-align: center;
        margin-top: 10%;
        animation: swing 3s ease-in-out infinite;
        display: block;
    }

    /* Estilo del título Dorado */
    .titulo {
        font-family: 'Georgia', serif;
        color: #FFD700; /* Dorado */
        text-align: center;
        font-size: 70px;
        font-weight: bold;
        text-shadow: 0px 0px 20px rgba(255, 215, 0, 0.5);
        margin-bottom: 20px;
    }

    /* Animación para que el girasol se mueva suavemente */
    @keyframes swing {
        0% { transform: rotate(-10deg); }
        50% { transform: rotate(10deg); }
        100% { transform: rotate(-10deg); }
    }
    
    /* Estilo para el botón */
    .stButton>button {
        background-color: #FFD700;
        color: black;
        border-radius: 20px;
        border: none;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
st.markdown('<div class="girasol">🌻</div>', unsafe_allow_html=True)
st.markdown('<p class="titulo">¡Feliz Cumpleaños!</p>', unsafe_allow_html=True)

# Botón centrado
_, col2, _ = st.columns([1,1,1])
with col2:
    if st.button('Haz clic aquí 🎂'):
        st.balloons()
        st.success("¡Que tengas un bonito dia!")
        st.success("No este triste estrellita")
        st.success("Espero y puedas cumplir todas tus metas, estoy muy orgulloso de ti, ahhhh estas creciendo muy rapido")
        st.success("Te mando un fuerte abracito")