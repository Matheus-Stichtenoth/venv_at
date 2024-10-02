import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import mplsoccer
from statsbombpy import sb

menu_lateral = ['Home',
                'Resultados de Campeonatos', 
                'Resultados de Partidas', 
                'Estatísticas do Jogador']

def color_page (color:str) -> None:
    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {color};
    }}
    </style>
    """, unsafe_allow_html=True)

def image_icones (url:str, tamanho = 100) -> None:
    st.image(url, width=tamanho)

def page_campeonatos() -> None:
    st.title('Resultados de Campeonatos 🏆')

    competitions = sb.competitions()
    competitions_names = competitions['competition_name'].unique()
    comp = st.selectbox('Selecione a competição ⬇:',competitions_names)
    comp_id = competitions[competitions['competition_name'] == comp]['competition_id'].values[0]

    seasons = competitions[competitions['competition_id'] == comp_id]['season_name'].unique()
    season_name = st.selectbox('Selecione a temporada ⬇:',seasons)
    season_id = competitions[competitions['season_name'] == season_name]['season_id'].values[0]

def page_partida() -> None:
    st.title('Resultados de Partidas ⚽')

    competitions = sb.competitions()
    competitions_names = competitions['competition_name'].unique()
    comp = st.selectbox('Selecione a competição ⬇:',competitions_names)
    comp_id = competitions[competitions['competition_name'] == comp]['competition_id'].values[0]

    seasons = competitions[competitions['competition_id'] == comp_id]['season_name'].unique()
    season_name = st.selectbox(f'Selecione a temporada da Competição {comp}:',seasons)
    season_id = competitions[competitions['season_name'] == season_name]['season_id'].values[0]

    matches = sb.matches(competition_id=comp_id,season_id = season_id)
    def get_match_label(match_id):
        row = matches[matches['match_id'] == match_id].iloc[0]
        return f'{row['match_date']} - {row['home_team']} vs {row['away_team']}'
    game = st.selectbox(f'Selecione uma Partida da Competição {comp} | Temporada: {season_name}',matches['match_id'],format_func = get_match_label)

    st.subheader(f'Competição {comp} | Temporada: {season_name}')

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        image_icones('https://cdn-icons-png.freepik.com/512/11818/11818132.png', tamanho = 50)

    with c2:
        arbitro = matches[matches['match_id'] == game]['referee'].values[0]
        st.markdown(f'<h5 style = "text-align: left;">{arbitro}</h5>', unsafe_allow_html=True)

    lc, rc = st.columns(2)
    with lc:
        st.write('Time da Casa')
        image_icones('https://cdn-icons-png.flaticon.com/256/88/88961.png')
        home_team = matches[matches['match_id'] == game]['home_team'].values[0]
        st.subheader(home_team)
        home_score = matches[matches['match_id'] == game]['home_score'].values[0]
        st.metric('Gols Marcados',home_score)

    with rc:
        st.write('Time Visitante')
        image_icones('https://cdn-icons-png.flaticon.com/256/912/912834.png')
        away_team = matches[matches['match_id'] == game]['away_team'].values[0]
        st.subheader(away_team)
        away_score = matches[matches['match_id'] == game]['away_score'].values[0]
        st.metric('Gols Marcados',away_score)

def page_jogador() -> None:
    st.title('Estatísticas do Jogador 👤')

def dashboard() -> None:
    st.title('Highlights Futebol!')
    choice = st.sidebar.selectbox('Páginas', menu_lateral)
    if choice == 'Resultados de Campeonatos':
        page_campeonatos()
    elif choice == 'Resultados de Partidas':
        page_partida()
    elif choice == 'Estatísticas do Jogador':
        page_jogador()
    elif choice == 'Home':
        st.write('Selecione a página que deseja visualizar no menu.')
        st.image('https://static.vecteezy.com/system/resources/previews/021/629/525/non_2x/icon-a-football-player-kicking-a-ball-free-png.png')
if __name__ == '__main__':
    dashboard()