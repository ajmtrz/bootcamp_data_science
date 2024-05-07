import streamlit as st
import pandas as pd
from typing import Any, List
from PIL import Image
import pages.src.plot_scripts as plots
import pages.src.eda_scripts as eda

st.set_page_config(layout='centered', page_icon='📊', page_title='PLayer Comparison')

st.write("# Players Comparison 📊")

cols = ['ID', 'Name', 'FullName', 'Nationality', 'BestPosition', 'Club', 'NationalTeam', 'PreferredFoot', 'Age',
        'Height',
        'Weight', 'Overall', 'Potential', 'Growth', 'PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal',
        'DefendingTotal', 'PhysicalityTotal', 'Crossing', 'Finishing', 'BallControl', 'Acceleration', 'SprintSpeed',
        'Agility', 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength', 'Aggression', 'Interceptions',
        'Positioning', 'Vision', 'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving',
        'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes', 'GKRating', 'PhotoUrl']

df_stats = pd.read_csv(r"data\players_fifa23.csv")

df_stats = eda.rename_cols(df_stats, cols)

player1 = st.selectbox('Buscar Jugador', set(df_stats.Name.to_list()))

player2 = st.selectbox('Buscar Jugador para comparar', set(df_stats.Name.to_list()))

col1, col2, col3, col4, col5 = st.columns([1, 1, 0.5, 1, 1])

with col1:
    st.image(df_stats[df_stats.Name == player1]['PhotoUrl'].values[0], width=150)

with col3:
    st.write('\n \n')
    st.write('\n \n')
    c1, c2, c3 = st.columns(3)
    with c2:
        st.title(':red[VS]')

with col5:
    st.image(df_stats[df_stats.Name == player2]['PhotoUrl'].values[0], width=150)

p1 = df_stats[df_stats.Name == player1][['Age', 'Weight', 'Height', 'Overall', 'BestPosition']]
p2 = df_stats[df_stats.Name == player2][['Age', 'Weight', 'Height', 'Overall', 'BestPosition']]

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    delta_age = int(p2.Age.values[0] - p1.Age.values[0])
    st.write(f'{player1} stats')
    st.metric(label='Age', value=p1.Age.values[0], delta=int(p1.Age.values[0]), delta_color="off")
    st.write(f'{player2} stats')
    st.metric(label='Age', value=p2.Age.values[0], delta=delta_age)
with c2:
    delta_age = int(p2.Weight.values[0] - p1.Weight.values[0])
    st.write(f'-')
    st.metric(label='Weight', value=p1.Weight.values[0], delta=int(p1.Weight.values[0]), delta_color="off")
    st.write(f'-')
    st.metric(label='Weight', value=p2.Weight.values[0], delta=delta_age)
with c3:
    delta_age = int(p2.Height.values[0] - p1.Height.values[0])
    st.write(f'-')
    st.metric(label='Height', value=p1.Height.values[0], delta=int(p1.Height.values[0]), delta_color="off")
    st.write(f'-')
    st.metric(label='Height', value=p2.Height.values[0], delta=delta_age)
with c4:
    delta_age = int(p2.Overall.values[0] - p1.Overall.values[0])
    st.write(f'-')
    st.metric(label='Overall', value=p1.Overall.values[0], delta=int(p1.Overall.values[0]), delta_color="off")
    st.write(f'-')
    st.metric(label='Overall', value=p2.Overall.values[0], delta=delta_age)
with c5:
    st.write(f'-')
    st.metric(label='Position', value=p1.BestPosition.values[0], delta=p1.BestPosition.values[0], delta_color="off" )
    st.write(f'-')
    st.metric(label='Position', value=p2.BestPosition.values[0], delta=p1.BestPosition.values[0])

plots.plot_pizza_chart_comparison(df_stats, player1, player2)
st.image('comparison_chart.png')
with open("comparison_chart.png", 'rb') as file:

    button = st.download_button(
        label='Donwnload Image',
        data=file,
        file_name=f'{player1}_vs_{player2}_info.png',
        mime= "image/png"
    )
