# pages/accueil.py
import streamlit as st

def show_accueil():
    
    # CSS personnalisé
    st.markdown("""
    <style>
    .hero {
        background: linear-gradient(135deg, #1a472a 0%, #f4a261 100%);
        padding: 3rem;
        border-radius: 30px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .hero h1 {
        font-size: 3rem;
        margin-bottom: 0.5rem;
    }
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Hero section
    st.markdown("""
    <div class="hero">
        <h1>🍲 SavorAfrik ✨</h1>
        <p>Savoure, Note et Partage les délices d'Afrique Centrale</p>
        <p>🇨🇲 🇨🇬 🇬🇦 🇨🇫 🇹🇩 🇬🇶</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Cartes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="card">
            <div style="font-size: 3rem;">📝</div>
            <h3>Donner mon avis</h3>
            <p>Note un plat et partage ton expérience</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="card">
            <div style="font-size: 3rem;">📊</div>
            <h3>Statistiques</h3>
            <p>Découvre les plats les mieux notés</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="card">
            <div style="font-size: 3rem;">🔍</div>
            <h3>Rechercher</h3>
            <p>Trouve des recettes traditionnelles</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="card">
            <div style="font-size: 3rem;">📋</div>
            <h3>Tous les avis</h3>
            <p>Consulte les retours des gourmands</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistiques rapides
    st.markdown("---")
    
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    
    with col_s1:
        st.metric("🍲 Plats à découvrir", "8+")
    with col_s2:
        st.metric("🌍 Pays", "6")
    with col_s3:
        st.metric("⭐ Note moyenne", "4.7/5")
    with col_s4:
        st.metric("📝 Avis", "À toi de jouer !")
    
    # Témoignage
    st.markdown("---")
    st.info("💬 *\"Avec SavorAfrik, j'ai redécouvert les plats de mon enfance !\" — Marie, 🇨🇲*")