# services/api_service.py
import requests
import streamlit as st
import random
import time

# API TheMealDB (gratuite, sans clé API)
THEMEALDB_API = "https://www.themealdb.com/api/json/v1/1/search.php?s="

# Images de fallback (si l'API ne trouve pas d'image)
FALLBACK_IMAGES = {
    "Cameroun": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg",
    "Congo": "https://images.pexels.com/photos/1279330/pexels-photo-1279330.jpeg",
    "Gabon": "https://images.pexels.com/photos/958545/pexels-photo-958545.jpeg",
    "RCA": "https://images.pexels.com/photos/1640774/pexels-photo-1640774.jpeg",
    "Tchad": "https://images.pexels.com/photos/1640772/pexels-photo-1640772.jpeg",
    "defaut": "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg"
}

# Base de données locale des plats africains (fallback si API ne trouve pas)
PLATS_LOCAUX = {
    "ndolé": {
        "nom": "Ndolé",
        "pays": "Cameroun",
        "description": "Plat national camerounais à base de feuilles de ndolé (feuilles amères), de crevettes séchées, de poisson fumé et d'huile de palme.",
        "instructions": "1. Laver et couper les feuilles de ndolé.\n2. Faire revenir les crevettes et le poisson.\n3. Ajouter les feuilles et l'huile de palme.\n4. Laisser mijoter 45 minutes.\n5. Servir avec du plantain ou du riz.",
        "ingredients": [
            "Feuilles de ndolé (ou épinards amers) : 1 kg",
            "Crevettes séchées : 200 g",
            "Poisson fumé : 300 g",
            "Oignons : 2",
            "Huile de palme : 500 ml",
            "Arachides moulues : 100 g",
            "Sel, piment"
        ],
        "temps_preparation": 90,
        "difficulte": "Moyenne"
    },
    "poulet dg": {
        "nom": "Poulet DG",
        "pays": "Cameroun",
        "description": "Le Poulet DG (Directeur Général) est un plat festif camerounais à base de poulet et de plantains frits.",
        "instructions": "1. Couper le poulet en morceaux et le faire dorer.\n2. Ajouter les oignons, tomates et carottes.\n3. Laisser mijoter.\n4. Faire frire les plantains séparément.\n5. Mélanger et servir.",
        "ingredients": [
            "Poulet : 1",
            "Plantains : 3",
            "Carottes : 3",
            "Oignons : 2",
            "Tomates : 3",
            "Huile : pour la friture",
            "Sel, poivre, ail"
        ],
        "temps_preparation": 60,
        "difficulte": "Facile"
    },
    "moamba nsusu": {
        "nom": "Moamba Nsusu",
        "pays": "Congo",
        "description": "Poulet à la sauce arachide, plat national du Congo. Une sauce onctueuse et riche en saveurs.",
        "instructions": "1. Faire dorer le poulet.\n2. Préparer la sauce arachide.\n3. Mijoter ensemble.\n4. Ajouter le gombo en fin de cuisson.\n5. Servir avec du riz ou du foufou.",
        "ingredients": [
            "Poulet : 1",
            "Pâte d'arachide : 3 c. à soupe",
            "Tomates : 3",
            "Oignons : 2",
            "Gombo : 200 g",
            "Huile de palme : 200 ml"
        ],
        "temps_preparation": 75,
        "difficulte": "Moyenne"
    },
    "sangah": {
        "nom": "Sangah",
        "pays": "Cameroun",
        "description": "Le Sangah est un plat traditionnel bamiléké à base de feuilles de manioc et de maïs moulu.",
        "instructions": "1. Laver les feuilles de manioc.\n2. Faire bouillir avec le maïs moulu.\n3. Ajouter l'huile de palme et le poisson fumé.\n4. Laisser cuire 40 minutes.\n5. Servir chaud.",
        "ingredients": [
            "Feuilles de manioc : 500 g",
            "Maïs moulu : 250 g",
            "Poisson fumé : 200 g",
            "Oignons : 2",
            "Huile de palme : 200 ml"
        ],
        "temps_preparation": 60,
        "difficulte": "Moyenne"
    },
    "koko": {
        "nom": "Koko",
        "pays": "RCA",
        "description": "Le Koko est un plat traditionnel centrafricain à base de feuilles de courge et d'arachides.",
        "instructions": "1. Laver les feuilles de courge.\n2. Concasser les arachides.\n3. Faire cuire ensemble avec le poisson fumé.\n4. Laisser mijoter 30 minutes.",
        "ingredients": [
            "Feuilles de courge : 500 g",
            "Arachides concassées : 200 g",
            "Poisson fumé : 200 g",
            "Oignons : 1",
            "Huile de palme : 150 ml"
        ],
        "temps_preparation": 45,
        "difficulte": "Facile"
    },
    "atanga": {
        "nom": "Atanga",
        "pays": "Gabon",
        "description": "L'Atanga est une pâte de graines sauvages, spécialité gabonaise souvent accompagnée de poisson ou de viande.",
        "instructions": "1. Faire cuire les graines d'atanga.\n2. Écraser les graines pour obtenir la pâte.\n3. Ajouter le poisson fumé et les crevettes.\n4. Assaisonner et mijoter.",
        "ingredients": [
            "Graines d'atanga (Dika) : 500 g",
            "Poisson fumé : 200 g",
            "Crevettes séchées : 100 g",
            "Piment : au goût"
        ],
        "temps_preparation": 60,
        "difficulte": "Difficile"
    }
}

def get_pays_depuis_nom(nom_plat):
    """Détermine le pays probable à partir du nom du plat"""
    nom_lower = nom_plat.lower()
    
    if "ndolé" in nom_lower or "ndole" in nom_lower or "poulet dg" in nom_lower or "sangah" in nom_lower:
        return "Cameroun"
    elif "moamba" in nom_lower:
        return "Congo"
    elif "koko" in nom_lower:
        return "RCA"
    elif "atanga" in nom_lower:
        return "Gabon"
    elif "maboke" in nom_lower:
        return "RCA"
    elif "miondo" in nom_lower:
        return "Cameroun"
    else:
        return "Afrique Centrale"

def chercher_recette_api(nom_plat):
    """Cherche une recette via TheMealDB API"""
    try:
        # Nettoyer le nom pour l'API
        query = nom_plat.replace(" ", "_").replace("é", "e").replace("è", "e")
        url = f"{THEMEALDB_API}{query}"
        
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if data and data.get("meals") and len(data["meals"]) > 0:
            meal = data["meals"][0]
            
            # Extraire les ingrédients
            ingredients = []
            for i in range(1, 21):
                ing = meal.get(f"strIngredient{i}")
                measure = meal.get(f"strMeasure{i}")
                if ing and ing.strip():
                    if measure and measure.strip():
                        ingredients.append(f"{measure} {ing}")
                    else:
                        ingredients.append(ing)
            
            # Extraire les instructions (3-4 phrases max)
            instructions = meal.get("strInstructions", "")
            if instructions:
                # Limiter à 500 caractères
                instructions = instructions[:500] + "..." if len(instructions) > 500 else instructions
            
            return {
                "trouve": True,
                "nom": meal.get("strMeal", nom_plat),
                "pays": get_pays_depuis_nom(nom_plat),
                "description": instructions[:300] if instructions else f"Le {nom_plat} est un plat traditionnel délicieux.",
                "instructions": instructions,
                "ingredients": ingredients[:8] if ingredients else ["Ingrédients non disponibles"],
                "image_url": meal.get("strMealThumb", FALLBACK_IMAGES["defaut"]),
                "temps_preparation": 60,
                "difficulte": "Moyenne",
                "source": "TheMealDB"
            }
    except Exception as e:
        print(f"Erreur API: {e}")
    
    return None

def chercher_recette_locale(nom_plat):
    """Cherche une recette dans la base locale"""
    nom_lower = nom_plat.lower()
    
    # Chercher correspondance exacte ou partielle
    for key, value in PLATS_LOCAUX.items():
        if key in nom_lower or nom_lower in key:
            return {
                "trouve": True,
                **value,
                "image_url": FALLBACK_IMAGES.get(value.get("pays", "defaut"), FALLBACK_IMAGES["defaut"]),
                "source": "Base locale SavorAfrik"
            }
    
    return None

def obtenir_infos_plat(nom_plat):
    """Fonction principale : récupère les infos du plat (API ou local)"""
    
    with st.spinner(f"🔍 Recherche de {nom_plat} dans notre bibliothèque..."):
        time.sleep(0.5)
        
        # 1. Essayer l'API TheMealDB
        resultat = chercher_recette_api(nom_plat)
        
        if resultat and resultat.get("trouve"):
            st.success(f"✅ Plat trouvé via {resultat['source']}")
            return resultat
        
        # 2. Sinon, utiliser la base locale
        resultat = chercher_recette_locale(nom_plat)
        
        if resultat and resultat.get("trouve"):
            st.info(f"📚 Plat trouvé dans la bibliothèque SavorAfrik")
            return resultat
        
        # 3. Si rien trouvé, générer une réponse par défaut
        st.warning(f"⚠️ Plat non trouvé. Voici une suggestion générique.")
        
        pays_probable = get_pays_depuis_nom(nom_plat)
        
        return {
            "trouve": True,
            "nom": nom_plat.title(),
            "pays": pays_probable,
            "description": f"Le {nom_plat} est un plat traditionnel de {pays_probable}. Sa recette varie selon les régions et les familles.",
            "instructions": f"La préparation du {nom_plat} demande des ingrédients frais et de la patience. Traditionnellement, ce plat se prépare avec des produits locaux et se déguste en famille ou entre amis.",
            "ingredients": [
                "Viande ou poisson frais",
                "Légumes locaux de saison",
                "Épices traditionnelles",
                "Huile végétale",
                "Sel, poivre"
            ],
            "image_url": FALLBACK_IMAGES.get(pays_probable, FALLBACK_IMAGES["defaut"]),
            "temps_preparation": 60,
            "difficulte": "Moyenne",
            "source": "Génération automatique"
        }

def get_stats_plats():
    """Retourne les statistiques des plats (pour le diagramme)"""
    return {
        "labels": ["Ndolé", "Poulet DG", "Moamba Nsusu", "Sangah", "Koko", "Atanga"],
        "notes": [4.9, 4.8, 4.7, 4.5, 4.3, 4.1],
        "couleurs": ["#1a472a", "#2d6a4f", "#f4a261", "#e76f51", "#f39c12", "#e67e22"]
    }