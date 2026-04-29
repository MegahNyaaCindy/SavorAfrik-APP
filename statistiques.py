# pages/statistiques.py
import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_tous_avis

def show_stats():
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1a472a, #2d6a4f); padding: 1rem; border-radius: 15px; margin-bottom: 1.5rem;">
        <h2 style="color: white; margin: 0;">📊 Analyses SavorAfrik</h2>
        <p style="color: #f4a261; margin: 0;">Découvre les tendances de la communauté</p>
    </div>
    """, unsafe_allow_html=True)
    
    df = get_tous_avis()
    
    if df.empty:
        st.info("📭 Aucun avis pour le moment. Sois la première à donner ton avis !")
        return
    
    # KPI
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📝 Nombre d'avis", len(df))
    with col2:
        st.metric("⭐ Note moyenne", f"{df['note'].mean():.1f}/5")
    with col3:
        taux = (df['recommandation'] == 'Oui').mean() * 100
        st.metric("👍 Taux recommandation", f"{taux:.0f}%")
    with col4:
        st.metric("🍲 Plats différents", df['plat'].nunique())
    
    st.markdown("---")
    
    # Graphiques
    col_g1, col_g2 = st.columns(2)
    
    with col_g1:
        fig_notes = px.histogram(df, x="note", title="Distribution des notes", 
                                  color_discrete_sequence=["#f4a261"])
        st.plotly_chart(fig_notes, use_container_width=True)
    
    with col_g2:
        fig_pays = px.bar(df, x="pays", title="Avis par pays",
                          color_discrete_sequence=["#1a472a"])
        st.plotly_chart(fig_pays, use_container_width=True)
    
    # Top plats
    top_plats = df.groupby('plat')['note'].mean().sort_values(ascending=False).head(5)
    fig_top = px.bar(x=top_plats.values, y=top_plats.index, orientation='h',
                     title="Top 5 des plats", labels={'x': 'Note moyenne', 'y': ''})
    st.plotly_chart(fig_top, use_container_width=True)