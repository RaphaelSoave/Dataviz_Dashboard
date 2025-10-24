import streamlit as st
import pandas as pd

def display(df):

    st.write("1970-2000 : It reveals a more concentrated pattern of closures, especially in Île-de-France and the northwestern regions of France. This indicates that closures were mainly focused on specific areas, possibly due to economic shifts, changes in the educational system, or other localized factors during this period.")
    st.write("2000-2025 : Shows a wider and more even distribution of closures across the country. There is a significant number of closures in both urban and rural areas. The closures are no longer concentrated in a few regions, indicating that the phenomenon has spread across a broader geographic area, possibly driven by nationwide educational reforms or demographic changes.")
    st.subheader("Trend overviews")
    
    # Graphiques ou tables de tendances
    st.write("Here's a look at the key trends observed in the data from closed establishments.")
    
    # Exemple de graphique
    st.subheader("Establishments closed over time")    
    df['year_fermeture'] = df['date_fermeture'].dt.year
    df_fermetures = df.groupby('year_fermeture').size().reset_index(name='Nombre de fermetures')
    st.line_chart(df_fermetures.set_index('year_fermeture'))
    st.write("It can be observed that from 1980, many schools closed. This can be explained by the implementation of educational reforms and rural relocations. A new peak occurred in 1992, with approximately 1,500 establishments closing. However, from 1995 onwards, there was a drastic drop in the number of closures. It is even possible to observe the consequences of COVID-19 in 2020, with the lowest number of closures, which was 452.")

    st.subheader("Closures by type of establishment")
    df_type = df.groupby('secteur_public_prive_libe')['date_fermeture'].count().reset_index(name='Nombre de fermetures')
    df_type['secteur_public_prive_libe'] = df_type['secteur_public_prive_libe'].map({0: 'Privé', 1: 'Public'})
    st.bar_chart(df_type.set_index('secteur_public_prive_libe'))
    st.write("The chart compares the number of closures between private and public establishments. Private establishments have a relatively low number of closures, with around 5,000, while public establishments experience a much higher number, close to 30,000. This suggests that public institutions are more affected by closures than private ones. The disparity could be due to factors like budget cuts, administrative changes, or other challenges that affect the public sector more significantly than the private sector.")

    st.subheader("Closures by school level")
    df_level = df.groupby('type_ecole')['date_fermeture'].count().reset_index(name='Nombre de fermetures')
    st.bar_chart(df_level.set_index('type_ecole'))
    st.write("It can be observed that preschools (maternelle) are by far the most affected by closures. This can be explained by several reasons. Firstly, the merging of schools: over time, there are fewer teachers, so classes become larger, and schools close as a result. Secondly, the format of preschools is becoming more similar to primary schools, leading to more closures of preschool classes. Meanwhile, primary and secondary schools see very few closures. This may be due to the fact that primary and secondary classes are already large, with an average of 40 students per class, which requires fewer teachers. As a result, closures are less common in primary and secondary schools.")    