import streamlit as st
import pandas as pd

def display(df):
    st.subheader("Detailed analyzes")
    
    # Comparaison des fermetures par région
    region_fermetures = df.groupby('libelle_region')['date_fermeture'].count().reset_index(name='Nombre de fermetures')
    st.bar_chart(region_fermetures.set_index('libelle_region'))
    st.write("The chart shows that the region with the most closures is 'Grand Est'. This can be explained by the movement of the population to larger cities and the decline in the youth population. Fewer students lead to the closure of classes. However, regions like Île-de-France, which have a large number of students, also show a high number of closures. This is because the region is constantly evolving, and it's natural that many schools close, but new ones also open. Thus, a point of balance is created. Additionally, all regions are facing budget cuts, which also contribute to the closures.")


