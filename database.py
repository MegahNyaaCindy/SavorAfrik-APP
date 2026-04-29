# database.py
import sqlite3
import pandas as pd
from datetime import datetime

DB_PATH = "data/avis.db"

def init_db():
    """Initialise la base de données"""
    import os
    os.makedirs("data", exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS avis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            plat TEXT,
            pays TEXT,
            note INTEGER,
            recommandation TEXT,
            temps_preparation INTEGER,
            commentaire TEXT
        )
    """)
    
    conn.commit()
    conn.close()

def ajouter_avis(plat, pays, note, recommandation, temps, commentaire):
    """Ajoute un avis"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO avis (date, plat, pays, note, recommandation, temps_preparation, commentaire)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (datetime.now().isoformat(), plat, pays, note, recommandation, temps, commentaire))
    
    conn.commit()
    conn.close()

def get_tous_avis():
    """Récupère tous les avis"""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM avis ORDER BY date DESC", conn)
    conn.close()
    return df