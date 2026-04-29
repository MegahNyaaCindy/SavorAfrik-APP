import streamlit as st
import requests
import time

st.set_page_config(page_title="SavorAfrik", page_icon="🍲", layout="wide")

# Style
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #1a472a, #f4a261);
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="hero"><h1 style="color:white;">🍲 SavorAfrik ✨</h1><p style="color:white;">Découvre les saveurs d\'Afrique Centrale</p></div>', unsafe_allow_html=True)

# Recherche
plat = st.text_input("🔍 Nom du plat :", placeholder="Ndolé, Poulet DG, Sangah...")

if plat:
    with st.spinner(f"Recherche de {plat}..."):
        time.sleep(1)
        
        # Simuler une réponse (à remplacer par ta vraie API)
        st.success(f"✅ Résultat pour : **{plat}**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image("https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg", use_container_width=True)
            st.markdown(f"**Pays :** Cameroun")
            st.markdown(f"**Temps :** 60 min")
        
        with col2:
            st.markdown("### 📖 Description")
            st.info(f"Le {plat} est un plat traditionnel d'Afrique Centrale.")
            st.markdown("### 🛒 Ingrédients")
            st.markdown("- Ingrédient 1\n- Ingrédient 2\n- Ingrédient 3")
            st.markdown("### 👩‍🍳 Préparation")
            st.markdown("1. Préparer les ingrédients\n2. Cuire\n3. Déguster !")
else:
    st.info("👆 Entrez le nom d'un plat pour voir sa recette")

st.markdown("---")
st.caption("TP INF232 - EC2 | SavorAfrik")