import matplotlib.pyplot as plt
import streamlit as st

def line_chart(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['year_fermeture'], data['Nombre de fermetures'])
    plt.title("Nombre d'établissements fermés au fil du temps")
    plt.xlabel("Année")
    plt.ylabel("Nombre de fermetures")
    plt.show()

def bar_chart(data):
    plt.figure(figsize=(10, 6))
    data.plot(kind='bar', x='libelle_region', y='Nombre de fermetures')
    plt.show()


import pydeck as pdk

def map_chart(df):
    # Créer un objet de la carte avec les coordonnées latitude/longitude
    st.subheader("Map of closed establishments")
    
    # Filtrer les données pour ne garder que celles avec des coordonnées valides
    df_valid = df.dropna(subset=['latitude', 'longitude'])
    
    # Créer la carte avec pydeck
    deck = pdk.Deck(
        # Vue de la carte
        initial_view_state=pdk.ViewState(
            latitude=46.603354,  # Latitude centrale de la France
            longitude=1.888334,  # Longitude centrale de la France
            zoom=6,  # Niveau de zoom
            pitch=0  # Inclinaison de la carte
        ),
        layers=[
            # Ajout des points représentant les établissements
            pdk.Layer(
                'ScatterplotLayer',  # Type de couche
                df_valid,
                get_position='[longitude, latitude]',
                get_radius=500,  # Taille des points
                get_fill_color=[255, 0, 0, 160],  # Couleur des points
                pickable=True  # Permet de cliquer sur les points
            )
        ]
    )

    # Afficher la carte
    st.pydeck_chart(deck)
