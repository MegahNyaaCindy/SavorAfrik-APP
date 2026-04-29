# pages/collecte.py
import streamlit as st
from database import ajouter_avis, init_db

# Initialiser la base de données
init_db()

def show_collecte():
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1a472a, #2d6a4f); padding: 1rem; border-radius: 15px; margin-bottom: 1.5rem;">
        <h2 style="color: white; margin: 0;">📝 Donner mon avis</h2>
        <p style="color: #f4a261; margin: 0;">Partage ton expérience culinaire</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("avis_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            plat = st.text_input("🍲 Nom du plat *", placeholder="Ex: Ndolé, Poulet DG...")
            pays = st.selectbox("🌍 Pays d'origine *", ["Cameroun", "Congo", "Gabon", "RCA", "Tchad", "Guinée Éq."])
            note = st.slider("⭐ Note (1 à 5)", 1, 5, 3)
        
        with col2:
            recommandation = st.radio("👍 Recommanderais-tu ce plat ?", ["Oui", "Non"])
            temps = st.number_input("⏱️ Temps de préparation (minutes)", min_value=0, max_value=300, value=60)
            commentaire = st.text_area("💬 Ton avis", placeholder="Délicieux, facile à préparer...")
        
        submitted = st.form_submit_button("✅ Envoyer mon avis", use_container_width=True)
        
        if submitted:
            if not plat:
                st.error("Veuillez entrer le nom du plat")
            else:
                ajouter_avis(plat, pays, note, recommandation, temps, commentaire)
                st.success(f"🎉 Merci pour ton avis sur {plat} !")
                st.balloons()