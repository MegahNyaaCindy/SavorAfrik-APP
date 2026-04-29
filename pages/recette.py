# pages/recette.py
import streamlit as st
import plotly.express as px
from services.api_service import obtenir_infos_plat, get_stats_plats

st.set_page_config(page_title="SavorAfrik - Recette", page_icon="🍲", layout="wide")

def show_recette():
    # Récupérer le plat depuis la session
    if 'plat_recherche' not in st.session_state:
        st.session_state['plat_recherche'] = None
    
    plat_nom = st.session_state.get('plat_recherche')
    
    if not plat_nom:
        st.warning("Aucun plat sélectionné. Retourne à l'accueil.")
        if st.button("🏠 Retour à l'accueil"):
            st.switch_page("app.py")
        return
    
    # CSS personnalisé
    st.markdown("""
    <style>
    .title-container {
        background: linear-gradient(135deg, #1a472a, #f4a261);
        padding: 1rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        text-align: center;
    }
    .info-card {
        background-color: #f8f9fa;
        border-radius: 12px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .ingredient-item {
        padding: 0.4rem;
        border-bottom: 1px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Obtenir les infos du plat
    plat_info = obtenir_infos_plat(plat_nom)
    
    # Titre
    st.markdown(f"""
    <div class="title-container">
        <h1 style="color: white;">🍲 {plat_info['nom']}</h1>
        <p style="color: rgba(255,255,255,0.9);">🇨🇲 {plat_info.get('pays', 'Afrique Centrale')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Deux colonnes
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        # Image
        st.image(plat_info.get('image_url', ''), use_container_width=True)
        
        # Informations rapides
        st.markdown("### 📋 Informations")
        st.markdown(f"⏱️ **Temps de préparation** : {plat_info.get('temps_preparation', 60)} minutes")
        st.markdown(f"⭐ **Difficulté** : {plat_info.get('difficulte', 'Moyenne')}")
        st.markdown(f"📎 **Source** : {plat_info.get('source', 'Base SavorAfrik')}")
        
        # Ingrédients
        st.markdown("### 🛒 Ingrédients")
        for ing in plat_info.get('ingredients', []):
            st.markdown(f"- {ing}")
    
    with col2:
        # Description
        st.markdown("### 📖 Description")
        st.info(plat_info.get('description', 'Aucune description disponible.'))
        
        # Instructions
        st.markdown("### 👩‍🍳 Préparation")
        
        if plat_info.get('instructions'):
            instructions = plat_info['instructions'].split('.')
            for i, instr in enumerate(instructions[:8], 1):
                if instr.strip():
                    st.markdown(f"**{i}.** {instr.strip()}.")
        else:
            st.markdown("Instructions non disponibles pour ce plat.")
        
        # Petit message
        st.caption("✨ La recette peut varier selon les traditions familiales.")
    
    st.markdown("---")
    
    # Diagramme des plats les plus appréciés
    st.markdown("### 📊 Classement des plats les plus appréciés d'Afrique Centrale")
    
    stats = get_stats_plats()
    
    fig = px.bar(
        x=stats["notes"],
        y=stats["labels"],
        orientation='h',
        title="Notes moyennes (sur 5)",
        labels={'x': 'Note moyenne', 'y': ''},
        color=stats["notes"],
        color_continuous_scale=['#f4a261', '#e76f51', '#1a472a'],
        text=stats["notes"]
    )
    
    fig.update_layout(
        height=400,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[0, 5.5], title="⭐ Note sur 5")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Bouton retour
    col_b1, col_b2, col_b3 = st.columns([1, 1, 1])
    with col_b2:
        if st.button("🏠 Nouvelle recherche", use_container_width=True):
            st.session_state['plat_recherche'] = None
            st.switch_page("app.py")

if __name__ == "__main__":
    show_recette()