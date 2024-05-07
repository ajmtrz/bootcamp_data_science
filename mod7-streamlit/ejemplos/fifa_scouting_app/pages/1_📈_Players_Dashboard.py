import streamlit as st
import pandas as pd
from PIL import Image
import pages.src.plot_scripts as plots
import pages.src.eda_scripts as eda


st.set_page_config(layout='centered', page_icon='📈', page_title='Players Dashboards')

st.write("# Players Dashboards 📈")

df1 = pd.read_csv(r"data\players_fifa23.csv")

cols = ['ID', 'Name', 'FullName','Nationality','BestPosition', 'Club', 'NationalTeam', 'PreferredFoot', 'Age', 'Height',
        'Weight','Overall', 'Potential', 'Growth', 'PaceTotal','ShootingTotal','PassingTotal','DribblingTotal',
        'DefendingTotal','PhysicalityTotal', 'Crossing', 'Finishing','BallControl', 'Acceleration', 'SprintSpeed',
        'Agility','Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength','Aggression', 'Interceptions',
        'Positioning', 'Vision','Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle','GKDiving',
        'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes','GKRating', 'PhotoUrl']

df1 = eda.rename_cols(df1, cols)
df = eda.rename_cols(pd.read_csv(r"data\players_distance_vr_1.csv"))

player = st.selectbox('Buscar Jugador', df1['Name'].to_list())

player_filter = df1[df1.Name == player]['FullName'].values[0]

club = df[df.player == player_filter]['club_logo'].values[0]

stats = df1[df1.Name == player]

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.image(stats.PhotoUrl.values[0], width=150)

with col2:
    st.write(f'## {stats.FullName.values[0]}')

with col3:
    st.image(club, width=100)

st.divider()

col4, col5, col6, col7 = st.columns(4)

with col4:
    foot = stats.PreferredFoot.values[0]
    st.write('### Prefered Foot')
    if foot == 'Right':
        foot_image = Image.open(r"data\images\pie_derecho.png")
    else:
        foot_image = Image.open(r"data\images\pie_izquierdo.png")
    st.image(foot_image)

with col5:
    # st.write("## :red[Age]")
    age_img = "https://cdn-icons-png.flaticon.com/512/10490/10490471.png"
    st.image(age_img)
    c1,c2,c3 = st.columns(3)
    with c2:
        st.write(f"# {stats.Age.values[0]}")

with col6:
    weight_img = 'https://www.supercoloring.com/sites/default/files/styles/coloring_medium/public/cif/2022/01' \
                 '/weighing-scale-coloring-page.png '
    st.image(weight_img)
    c1, c2, c3 = st.columns(3)
    with c2:
        st.write(f"# {stats.Weight.values[0]}")

with col7:
    height_img = 'https://us.123rf.com/450wm/theerakit/theerakit2202/theerakit220200080/182793824-icono-de-escala' \
                 '-alta-de-hombre-sobre-fondo-blanco-se%C3%B1al-de-altura-s%C3%ADmbolo-de-persona-alta-estilo.jpg?ver' \
                 '=6 '
    st.image(height_img)
    c1, c2, c3 = st.columns(3)
    with c2:
        st.write(f"# {stats.Height.values[0]}")

st.divider()

plots.plot_player_info(df1, player)

st.image('info.png')

with open("info.png", 'rb') as file:

    button = st.download_button(
        label='Donwnload Image',
        data=file,
        file_name=f'{player}_info.png',
        mime= "image/png"
    )