import streamlit as st
import pandas as pd
from utils.io import load_data
from utils.prep import clean_data
from utils.viz import map_chart 
from sections import intro, overview, deep_dives, conclusions

# Chargement des données
@st.cache_data(show_spinner=False)
def get_data():
    df_raw = load_data()
    df_clean = clean_data(df_raw)
    return df_clean


st.set_page_config(page_title="Data Storytelling: Établissements Fermés", layout="wide")
df = get_data()


st.title("Data Storytelling: Fermetures d'Établissements en France")
st.sidebar.header("Filters")

# Filtre 
regions = st.sidebar.multiselect("Select one or more regions", df["libelle_region"].unique())

min_year = df['year_fermeture'].min()
max_year = df['year_fermeture'].max()
year_range = st.sidebar.slider(
    "Year range",
    min_value=int(min_year),
    max_value=int(max_year),
    value=(int(min_year), int(max_year)),
    help="Select the period to analyse"
)


school_type = st.sidebar.selectbox("Select the type of establishment", ['Tous', 'Public', 'Privé'])


school_level = st.sidebar.selectbox("Select school level", ['Tous', 'Maternelle', 'Primaire', 'Secondaire'])


df_filtered = df.copy()

if regions:
    df_filtered = df_filtered[df_filtered["libelle_region"].isin(regions)]


if year_range:    
    df_filtered = df_filtered[
        (df_filtered['year_fermeture'] >= year_range[0]) &
        (df_filtered['year_fermeture'] <= year_range[1])
    ]

if school_type == 'Public':
    df_filtered = df_filtered[df_filtered['secteur_public_prive_libe'] == 1]
elif school_type == 'Privé':
    df_filtered = df_filtered[df_filtered['secteur_public_prive_libe'] == 0]

if school_level != 'Tous':
    df_filtered = df_filtered[df_filtered['type_ecole'] == school_level]

# KPI Header
st.header("Key Performance Indicators")
c1, c2, c3 = st.columns(3)
c1.metric("Total établissements", len(df_filtered))
c2.metric("Établissements fermés", df_filtered[df_filtered['date_fermeture'].notnull()].shape[0])
c3.metric("Régions disponibles", len(df_filtered["libelle_region"].unique()))

# Affichage des section
intro.display()

# Affichage de la carte
map_chart(df_filtered)



overview.display(df_filtered)

deep_dives.display(df_filtered)

conclusions.display()


