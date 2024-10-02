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
    st.selectbox(f'Selecione uma Partida da Competição {comp} | Temporada: {season_name}',matches['match_id'],format_func = get_match_label)

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