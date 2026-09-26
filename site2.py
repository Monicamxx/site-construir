import streamlit as st

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="CONSTRUIR+ | Conectando Profissionais",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS CUSTOMIZADO (Visual do Figma) ---
st.markdown("""
<style>
    /* Esconde os menus padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}

    /* Fundo geral */
    .stApp { background-color: #F8F9FA; }

    /* --- ESTILO DOS BOTÕES DO MENU (Para parecerem links) --- */
    div.stButton > button {
        background-color: transparent !important;
        color: #2c1b8f !important;
        border: none !important;
        font-weight: 800 !important;
        font-size: 14px !important;
        letter-spacing: 1px !important;
        padding: 0px !important;
        margin: 0px !important;
        box-shadow: none !important;
    }
    div.stButton > button:hover {
        color: #1a0f5c !important;
        text-decoration: underline !important;
    }

    /* --- BOTÕES ROXOS (ENTRAR / CADASTRAR) --- */
    .btn-roxo {
        display: block;
        background-color: #2c1b8f;
        color: white !important;
        padding: 10px 25px;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        font-size: 14px;
        width: 100%;
        transition: background-color 0.3s;
    }
    .btn-roxo:hover {
        background-color: #1a0f5c;
        color: white !important;
        text-decoration: none;
    }

    /* --- SEÇÃO HERO (Banner) --- */
    .hero-section {
        position: relative;
        background-image: url('https://images.unsplash.com/photo-1541888946425-d81bb19240f5?q=80&w=2070&auto=format&fit=crop');
        background-size: cover; background-position: center;
        padding: 80px 50px 100px 50px;
        display: flex; flex-direction: column; justify-content: center;
    }
    .hero-section::before {
        content: ""; position: absolute; top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(90deg, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.7) 40%, rgba(255,255,255,0) 100%);
    }
    .hero-text { position: relative; z-index: 1; max-width: 600px; }
    .hero-text h1 {
        color: #2c1b8f; font-size: 46px; font-weight: 900;
        line-height: 1.1; margin-bottom: 15px; text-transform: uppercase;
    }
    .hero-text p { color: #2c1b8f; font-size: 18px; font-weight: 600; }

    /* --- BLOCOS DE CATEGORIA --- */
    .categoria-box {
        background-color: white; border-radius: 8px; padding: 20px;
        display: flex; align-items: center; justify-content: center; gap: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 120px; margin-bottom: 20px;
    }
    .categoria-box h4 { color: #2c1b8f; margin: 0; font-size: 16px; font-weight: 800; }
    .titulo-secao { color: #2c1b8f; font-size: 24px; font-weight: 900; margin-top: 40px; margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)


# --- 3. INICIALIZA O ESTADO DA PÁGINA ---
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'Inicio'

# --- 4. CAPTURA O CLIQUE DOS LINKS (LOGIN E CADASTRO) ---
query_params = st.query_params
if "pagina" in query_params:
    if query_params["pagina"] == "Login":
        st.session_state.pagina = 'Login'
    elif query_params["pagina"] == "Cadastro":
        st.session_state.pagina = 'Cadastro'
    st.query_params.clear()
    st.rerun()

# --- 5. CABEÇALHO (NAVBAR no TOPO) ---
col_logo, col_m1, col_m2, col_m3, col_m4, col_btn1, col_btn2 = st.columns([2, 1, 1, 1, 1, 1, 1])

with col_logo:
    st.image("logo.png", width=120) # Ajuste a largura (width) como preferir

with col_m1:
    if st.button("INICIO"): st.session_state.pagina = 'Inicio'; st.rerun()
with col_m2:
    if st.button("VAGAS"): st.session_state.pagina = 'Vagas'; st.rerun()
with col_m3:
    if st.button("EMPRESAS"): st.session_state.pagina = 'Empresas'; st.rerun()
with col_m4:
    if st.button("PROFISSIONAIS"): st.session_state.pagina = 'Profissionais'; st.rerun()

with col_btn1:
    st.markdown('<a href="?pagina=Login" target="_self" class="btn-roxo">ENTRAR</a>', unsafe_allow_html=True)

with col_btn2:
    st.markdown('<a href="?pagina=Cadastro" target="_self" class="btn-roxo">CADASTRAR</a>', unsafe_allow_html=True)

st.markdown("<hr style='margin: 0 0 20px 0; border: 1px solid #eee;'>", unsafe_allow_html=True)


# --- 6. CONTEÚDO DAS PÁGINAS ---

if st.session_state.pagina == 'Inicio':
    # ================== PÁGINA INICIAL ==================
    st.markdown("""
    <div class="hero-section">
        <div class="hero-text">
            <h1>CONECTANDO<br>PROFISSIONAIS A<br>CONSTRUÇÃO CIVIL</h1>
            <p>Encontre profissionais qualificados ou<br>encontre sua próxima oportunidade.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    col_vazia1, col_busca, col_vazia2 = st.columns([1, 8, 1])
    with col_busca:
        c1, c2, c3 = st.columns([3, 2, 1])
        with c1:
            termo = st.text_input("Buscar", placeholder="🔍 Buscar profissional ou vaga", label_visibility="collapsed")
        with c2:
            local = st.text_input("Local", placeholder="📍 Localização", label_visibility="collapsed")
        with c3:
            if st.button("BUSCAR", use_container_width=True, type="primary"):
                st.success(f"Buscando por '{termo}' em '{local}'...")

    st.write("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="categoria-box"><img src="https://cdn-icons-png.flaticon.com/512/921/921513.png" width="60"><h4>PARA PROFISSIONAIS</h4></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="categoria-box"><img src="https://cdn-icons-png.flaticon.com/512/3063/3063822.png" width="60"><h4>PARA EMPRESAS</h4></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="categoria-box"><img src="https://cdn-icons-png.flaticon.com/512/1000/1000961.png" width="60"><h4>CONEXÃO</h4></div>""", unsafe_allow_html=True)

    st.markdown("<div class='titulo-secao'>Demanda do Mercado</div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.image("https://images.unsplash.com/photo-1621905251189-08b45d6a269e?q=80&w=2069&auto=format&fit=crop", use_container_width=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1504307651254-35680f356dfd?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
    with c3:
        st.image("https://images.unsplash.com/photo-1581094794329-c8112a89af12?q=80&w=2070&auto=format&fit=crop", use_container_width=True)
        st.markdown("<p style='text-align: center; color: #2c1b8f; font-weight: bold;'>Engenheiros</p>", unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div style="background-color: white; border: 1px solid #ddd; border-radius: 8px; padding: 20px; text-align: center; height: 100%; display: flex; flex-direction: column; justify-content: center;">
            <img src="https://cdn-icons-png.flaticon.com/512/1067/1067357.png" width="80" style="margin: 0 auto 10px auto;">
            <h2 style="color: #2c1b8f; margin: 0; font-weight: 900;">CONSTRUIR+</h2>
            <p style="color: #555; font-size: 10px; font-weight: bold; margin-top: 5px;">PLATAFORMA DE CAPTAÇÃO DE PROFISSIONAIS QUALIFICADOS</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.pagina == 'Vagas':
    # ================== PÁGINA DE VAGAS ==================
    st.markdown("<h1 style='color: #2c1b8f;'>💼 Vagas Disponíveis</h1>", unsafe_allow_html=True)
    st.write("Confira as oportunidades mais recentes na construção civil:")
    
    vagas = [
        {"titulo": "Engenheiro Civil", "empresa": "Construtora Alpha", "local": "São Paulo - SP"},
        {"titulo": "Mestre de Obras", "empresa": "Edifica Engenharia", "local": "Rio de Janeiro - RJ"},
        {"titulo": "Eletricista Predial", "empresa": "InstalaTech", "local": "Belo Horizonte - MG"},
    ]
    for vaga in vagas:
        st.markdown(f"""
        <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 15px; border-left: 5px solid #2c1b8f;">
            <h3 style="color: #2c1b8f; margin: 0 0 5px 0;">{vaga['titulo']}</h3>
            <p style="color: #555; margin: 0;"><strong>Empresa:</strong> {vaga['empresa']} | <strong>Local:</strong> {vaga['local']}</p>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.pagina == 'Empresas':
    # ================== PÁGINA DE EMPRESAS ==================
    st.markdown("<h1 style='color: #2c1b8f;'>🏢 Para Empresas</h1>", unsafe_allow_html=True)
    st.write("Encontre os melhores profissionais para a sua obra de forma rápida e segura.")
    st.write("---")
    st.markdown("<h3 style='color: #2c1b8f;'>Por que usar a Construir+?</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%;">
            <h4 style="color: #2c1b8f; margin-top: 0;">✅ Profissionais Verificados</h4>
            <p style="color: #555; font-size: 14px;">Todos os profissionais passam por uma análise de currículo e documentação antes de serem exibidos na plataforma.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%;">
            <h4 style="color: #2c1b8f; margin-top: 0;">⚡ Busca Rápida</h4>
            <p style="color: #555; font-size: 14px;">Filtre por especialidade, localização e experiência para encontrar o profissional ideal em minutos.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%;">
            <h4 style="color: #2c1b8f; margin-top: 0;">📋 Gestão de Vagas</h4>
            <p style="color: #555; font-size: 14px;">Publique suas vagas e gerencie os candidatos diretamente pela nossa plataforma.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<h3 style='color: #2c1b8f;'>Empresas Parceiras</h3>", unsafe_allow_html=True)
    st.write("Veja algumas das empresas que já confiam na Construir+:")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("<div style='background-color: white; border: 1px solid #eee; border-radius: 8px; padding: 20px; text-align: center; color: #555; font-weight: bold;'>Construtora Alpha</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='background-color: white; border: 1px solid #eee; border-radius: 8px; padding: 20px; text-align: center; color: #555; font-weight: bold;'>Edifica Engenharia</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div style='background-color: white; border: 1px solid #eee; border-radius: 8px; padding: 20px; text-align: center; color: #555; font-weight: bold;'>InstalaTech</div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div style='background-color: white; border: 1px solid #eee; border-radius: 8px; padding: 20px; text-align: center; color: #555; font-weight: bold;'>Sua Empresa Aqui</div>", unsafe_allow_html=True)

elif st.session_state.pagina == 'Profissionais':
    # ================== PÁGINA DE PROFISSIONAIS ==================
    st.markdown("<h1 style='color: #2c1b8f;'>👷 Para Profissionais</h1>", unsafe_allow_html=True)
    st.write("Encontre a oportunidade perfeita para a sua carreira na construção civil.")
    st.write("---")
    st.markdown("<h3 style='color: #2c1b8f;'>Como funciona para você?</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%; text-align: center;">
            <h2 style="color: #2c1b8f; margin: 0;">1️⃣</h2>
            <h4 style="color: #2c1b8f; margin: 10px 0;">Cadastre-se</h4>
            <p style="color: #555; font-size: 14px;">Crie seu perfil gratuitamente com suas experiências e certificações.</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%; text-align: center;">
            <h2 style="color: #2c1b8f; margin: 0;">2️⃣</h2>
            <h4 style="color: #2c1b8f; margin: 10px 0;">Busque Vagas</h4>
            <p style="color: #555; font-size: 14px;">Encontre vagas compatíveis com sua especialidade e localização.</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="background-color: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); height: 100%; text-align: center;">
            <h2 style="color: #2c1b8f; margin: 0;">3️⃣</h2>
            <h4 style="color: #2c1b8f; margin: 10px 0;">Seja Contratado</h4>
            <p style="color: #555; font-size: 14px;">As empresas entram em contato diretamente com você.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("---")
    st.markdown("<h3 style='color: #2c1b8f;'>Áreas em Destaque</h3>", unsafe_allow_html=True)
    
    areas = ["🔨 Pedreiro", "⚡ Eletricista", "🚿 Encanador", "🏗️ Engenheiro Civil", "📐 Arquiteto", "🖌️ Pintor", "🚛 Operador de Máquinas", "🧱 Azulejista"]
    
    cols = st.columns(4)
    for i, area in enumerate(areas):
        with cols[i % 4]:
            st.markdown(f"""
            <div style="background-color: #f0f2f6; border-radius: 8px; padding: 15px; margin-bottom: 10px; text-align: center; color: #2c1b8f; font-weight: bold;">
                {area}
            </div>
            """, unsafe_allow_html=True)

elif st.session_state.pagina == 'Cadastro':
    # ================== PÁGINA DE CADASTRO ==================
    st.markdown("<h1 style='color: #2c1b8f; text-align: center;'>📝 Criar Conta</h1>", unsafe_allow_html=True)
    st.write("Preencha os dados abaixo para se cadastrar na Construir+.")
    
    col_vazia1, col_form, col_vazia2 = st.columns([1, 2, 1])
    with col_form:
        with st.form("form_cadastro"):
            nome = st.text_input("Nome Completo")
            email = st.text_input("E-mail")
            senha = st.text_input("Senha", type="password")
            confirmar_senha = st.text_input("Confirmar Senha", type="password")
            
            botao_cadastrar = st.form_submit_button("CADASTRAR", use_container_width=True)
            
            if botao_cadastrar:
                if nome and email and senha and (senha == confirmar_senha):
                    st.success(f"✅ Cadastro de {nome} realizado com sucesso! Agora faça o login.")
                else:
                    st.error("Por favor, preencha todos os campos e garanta que as senhas coincidam.")

elif st.session_state.pagina == 'Login':
    # ================== PÁGINA DE LOGIN ==================
    st.markdown("<h1 style='color: #2c1b8f; text-align: center;'>🔐 Entrar</h1>", unsafe_allow_html=True)
    st.write("Acesse sua conta para continuar.")
    
    col_vazia1, col_form, col_vazia2 = st.columns([1, 2, 1])
    with col_form:
        with st.form("form_login"):
            email_login = st.text_input("E-mail")
            senha_login = st.text_input("Senha", type="password")
            
            botao_login = st.form_submit_button("ENTRAR", use_container_width=True)
            
            if botao_login:
                if email_login and senha_login:
                    st.success(f"✅ Login realizado com sucesso! Bem-vindo, {email_login}.")
                else:
                    st.error("Por favor, preencha o e-mail e a senha.")
