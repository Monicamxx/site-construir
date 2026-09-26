
import streamlit as st

# --- CSS BÁSICO ---
st.markdown("""
<style>
    .titulo-pagina { color: #2c1b8f; font-size: 40px; font-weight: 900; margin-bottom: 20px; }
    .texto-destaque { font-size: 18px; color: #333; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

# --- CONTEÚDO DA PÁGINA ---
st.markdown("<div class='titulo-pagina'>👷 Para Profissionais</div>", unsafe_allow_html=True)

st.markdown("""
<div class="texto-destaque">
    <p>Bem-vindo à área dedicada aos profissionais da construção civil.</p>
    <p>Aqui você pode:</p>
    <ul>
        <li>Criar seu perfil profissional.</li>
        <li>Buscar vagas compatíveis com sua experiência.</li>
        <li>Capacitar-se com nossos cursos.</li>
    </ul>
    <p>Em breve, esta seção estará completa com todas as funcionalidades.</p>
</div>
""", unsafe_allow_html=True)

st.info("💡 Área em desenvolvimento. Fique atento às novidades!")