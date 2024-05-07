import streamlit as st
import pandas as pd
from typing import Any, List
from PIL import Image
import pages.src.plot_scripts as plots
import pages.src.eda_scripts as eda


st.set_page_config(layout='centered', page_icon='🌍', page_title='PLayer Search')

st.write("# Players Search 🌍")

df = pd.read_csv(r'data\players_distance_vr_1.csv')
df_stats = pd.read_csv(r"data\players_fifa23.csv")

player = st.selectbox('Buscar Jugador', set(df.player.to_list()))

cols = ['FullName', 'Overall', 'Potential', 'ValueEUR', 'ReleaseClause']

player_comp = df_stats[cols]

stats = df[df.player == player]

p_overall = int(player_comp[player_comp.FullName == player].Overall.values[0])
p_value = int(player_comp[player_comp.FullName == player].ValueEUR.values[0])
p_potential = int(player_comp[player_comp.FullName == player].Potential.values[0])
p_clause = int(player_comp[player_comp.FullName == player].ReleaseClause.values[0])

col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.image(stats.photo.values[0], width=100)

with col2:
    st.write(f'# {stats.player.values[0]}')

with col3:
    st.image(stats.club_logo.values[0], width=75)

col4, col5, col6, col7 = st.columns(4)

with col4:

    st.metric(label='Value', value=p_overall, delta=p_overall, delta_color="off")

with col5:

    st.metric(label='Overall', value=p_overall, delta=p_overall, delta_color="off")

with col6:

    st.metric(label='Potential', value=p_potential, delta=p_potential, delta_color="off")

with col7:

    st.metric(label='Clause', value=p_clause, delta=p_clause, delta_color="off")

st.divider()

st.title('Most Similar Players :fire:')

st.divider()

for i in range(5):
    vs_player = player_comp[player_comp.FullName == stats.player_compare.values[i]]

    vs_p_overall = int(vs_player[vs_player.FullName == stats.player_compare.values[i]].Overall.values[0])
    vs_p_value = int(vs_player[vs_player.FullName == stats.player_compare.values[i]].ValueEUR.values[0])
    vs_p_potential = int(vs_player[vs_player.FullName == stats.player_compare.values[i]].Potential.values[0])
    vs_p_clause = int(vs_player[vs_player.FullName == stats.player_compare.values[i]].ReleaseClause.values[0])

    col1, col2, col3 = st.columns([1,2,1])

    with col1:
        st.image(stats.player_compare_photo.values[i], width=100)

    with col2:
        st.write(f'# {stats.player_compare.values[i]}')

    with col3:
        st.image(stats.player_compare_club_logo.values[i], width=75)

    col4, col5, col6, col7 = st.columns(4)

    with col4:

        delta_v =  vs_p_value -p_value
        st.metric(label='Value', value=vs_p_value, delta=delta_v)

    with col5:

        delta_o = vs_p_overall - p_overall
        st.metric(label='Overall', value=vs_p_overall, delta=delta_o)

    with col6:

        delta_p = vs_p_potential - p_potential
        st.metric(label='Potential', value=vs_p_potential, delta=delta_p)

    with col7:

        delta_c = vs_p_clause - p_clause
        st.metric(label='Clause', value=vs_p_clause, delta=delta_c)

    st.divider()