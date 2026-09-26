import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="CONSTRUIR+ | Conectando Profissionais",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS CUSTOMIZADO (Para replicar o design exato) ---
st.markdown("""
<style>
    /* Esconde os menus padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fundo geral do site */
    .stApp {
        background-color: #F8F9FA; /* Cinza bem claro para destacar os blocos brancos */
    }

    /* --- NAVBAR (Menu Superior) --- */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 50px;
        background-color: white;
    }
    .nav-links {
        display: flex;
        gap: 40px;
        font-weight: 800;
        color: #2c1b8f;
        font-size: 14px;
        letter-spacing: 1px;
    }
    
    /* --- SEÇÃO HERO (Banner) --- */
    .hero-section {
        position: relative;
        /* Imagem de fundo: Engenheiro olhando para construção */
        background-image: url('https://images.unsplash.com/photo-1541888946425-d81bb19240f5?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        padding: 80px 50px 100px 50px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .hero-section::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(90deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.7) 40%, rgba(255,255,255,0) 100%);
    }
    .hero-text {
        position: relative;
        z-index: 1;
        max-width: 600px;
    }
    .hero-text h1 {
        color: #2c1b8f;
        font-size: 46px;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 15px;
        text-transform: uppercase;
    }
    .hero-text p {
        color: #2c1b8f;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 0;
    }
    
    /* --- BOTÕES PERSONALIZADOS --- */
    .btn-roxo {
        background-color: #2c1b8f;
        color: white !important;
        border: none;
        padding: 10px 25px;
        border-radius: 5px;
        font-weight: bold;
        text-decoration: none;
        font-size: 14px;
        text-align: center;
    }

    /* --- BLOCOS DE CATEGORIA (Para Profissionais, Empresas, Conexão) --- */
    .categoria-box {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        height: 120px;
        margin-bottom: 20px;
    }
    .categoria-box h4 {
        color: #2c1b8f;
        margin: 0;
        font-size: 16px;
        font-weight: 800;
    }

    /* --- TÍTULOS DE SEÇÃO --- */
    .titulo-secao {
        color: #2c1b8f;
        font-size: 24px;
        font-weight: 900;
        margin-top: 40px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# --- 3. CABEÇALHO (NAVBAR) ---
st.markdown("""
<div class="navbar">
    <div style="display: flex; align-items: center; gap: 10px;">
        <img src="https://cdn-icons-png.flaticon.com/512/1067/1067357.png" width="50">
        <div>
            <h3 style="margin:0; color:#2c1b8f; font-weight: 900; font-size: 22px;">CONSTRUIR+</h3>
            <span style="font-size:8px; color:#555; font-weight: bold;">PLATAFORMA DE CAPTAÇÃO DE PROFISSIONAIS QUALIFICADOS NA CONSTRUÇÃO CIVIL</span>
        </div>
    </div>
    <div class="nav-links">
        <span>INICIO</span>
        <span>VAGAS</span>
        <span>EMPRESAS</span>
        <span>PROFISSIONAIS</span>
    </div>
    <div style="display: flex; gap: 15px;">
        <a href="#" class="btn-roxo">ENTRAR</a>
        <a href="#" class="btn-roxo">CADASTRAR</a>
    </div>
</div>
""", unsafe_allow_html=True)


# --- 4. SEÇÃO HERO (Imagem e Texto Principal) ---
st.markdown("""
<div class="hero-section">
    <div class="hero-text">
        <h1>CONECTANDO<br>PROFISSIONAIS A<br>CONSTRUÇÃO CIVIL</h1>
        <p>Encontre profissionais qualificados ou<br>encontre sua próxima oportunidade.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 5. BARRA DE BUSCA DUPLA (Sobrepondo a imagem) ---
# Usamos colunas vazias nas laterais para centralizar a barra
st.write("")
col_vazia1, col_busca, col_vazia2 = st.columns([1, 8, 1])

with col_busca:
    # Colunas internas: Profissional | Localização | Botão
    c1, c2, c3 = st.columns([3, 2, 1])
    
    with c1:
        termo = st.text_input("Buscar", placeholder="🔍 Buscar profissional ou vaga", label_visibility="collapsed")
    with c2:
        local = st.text_input("Local", placeholder="📍 Localização", label_visibility="collapsed")
    with c3:
        if st.button("BUSCAR", use_container_width=True, type="primary"):
            st.success(f"Buscando por '{termo}' em '{local}'...")

st.write("---")

# --- 6. SEÇÃO DE CATEGORIAS (Blocos Brancos) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="categoria-box">
        <img src="https://cdn-icons-png.flaticon.com/512/921/921513.png" width="60">
        <h4>PARA PROFISSIONAIS</h4>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="categoria-box">
        <img src="https://cdn-icons-png.flaticon.com/512/3063/3063822.png" width="60">
        <h4>PARA EMPRESAS</h4>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="categoria-box">
        <img src="https://cdn-icons-png.flaticon.com/512/1000/1000961.png" width="60">
        <h4>CONEXÃO</h4>
    </div>
    """, unsafe_allow_html=True)


# --- 7. SEÇÃO "DEMANDA DO MERCADO" (Galeria de Fotos) ---
st.markdown("<div class='titulo-secao'>Demanda do Mercado</div>", unsafe_allow_html=True)

# Criando 4 colunas para as fotos
c1, c2, c3, c4 = st.columns(4)

with c1:
    # Foto 1: Eletricista
    st.image("https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=2069&auto=format&fit=crop", use_container_width=True)

with c2:
    # Foto 2: Pedreiro
    st.image("https://images.unsplash.com/photo-1504307651254-35680f356dfd?q=80&w=2070&auto=format&fit=crop", use_container_width=True)

with c3:
    # Foto 3: Engenheiros (com legenda)
    st.image("https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
    st.markdown("<p style='text-align: center; color: #2c1b8f; font-weight: bold;'>Engenheiros</p>", unsafe_allow_html=True)

with c4:
    # Foto 4: Logo Construir+ (Simulada com um card)
    st.markdown("""
    <div style="background-color: white; border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center;">
        <img src="https://cdn-icons-png.flaticon.com/512/1067/1067357.png" width="80" style="margin: 0 auto 10px auto;">
        <h2 style="color: #2c1b8f; margin: 0; font-weight: 900;">CONSTRUIR+</h2>
        <p style="color: #555; font-size: 10px; font-weight: bold; margin-top: 5px;">PLATAFORMA DE CAPTAÇÃO DE PROFISSIONAIS QUALIFICADOS NA CONSTRUÇÃO CIVIL</p>
    </div>
    """, unsafe_allow_html=True)