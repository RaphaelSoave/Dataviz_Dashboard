import pandas as pd
import numpy as np
import unicodedata


def clean_data(df):
    # Conversion des dates en datetime
    df['date_ouverture'] = pd.to_datetime(df['date_ouverture'], errors='coerce')
    df['date_fermeture'] = pd.to_datetime(df['date_fermeture'], errors='coerce')
    
    # Gestion des valeurs manquantes pour les colonnes importantes
    df['localite_acheminement_uai'].fillna('Inconnue', inplace=True)
    df['appellation_officielle'].fillna('Inconnu', inplace=True)
    df['denomination_principale'].fillna('Inconnu', inplace=True)
    
    # Utilise la moyenne Pour les colonnes numériques avec des valeurs manquantes
    df['latitude'].fillna(df['latitude'].mean(), inplace=True)
    df['longitude'].fillna(df['longitude'].mean(), inplace=True)
    
    # Traitement des colonnes avec une grande proportion de valeurs manquantes
    df.drop(columns=['boite_postale_uai'], inplace=True)
    
    # Conversion des codes postaux et des autres colonnes catégorielles en type catégorie
    df['code_postal_uai'] = df['code_postal_uai'].astype(str)
    df['libelle_region'] = df['libelle_region'].astype('category')
    
    
    # Enlever les doublons éventuels
    df.drop_duplicates(inplace=True)
    
    # Ajoute des colonnes supplémentaires
    df['year_ouverture'] = df['date_ouverture'].dt.year
    df['year_fermeture'] = df['date_fermeture'].dt.year
    

    df['secteur_public_prive_libe'] = df['secteur_public_prive_libe'].map({
        'Public': 1, 'Privé': 0
    }).fillna(-1)  # Valeur -1 pour les inconnus ou erreurs

    df['type_ecole'] = df.apply(
    lambda row: 'Maternelle' if row['Ecole_maternelle'] == 1 else                    
    ('Primaire' if row['Ecole_elementaire'] == 1 else 'Secondaire'),
    axis=1
    )


    return df

    
