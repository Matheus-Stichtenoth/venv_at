import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import mplsoccer
import statsbombpy

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

def page_partida() -> None:
    st.title('Resultados de Partidas ⚽')

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
        st.write('Selecione a página que deseja visualizar ao lado.')
        st.image('https://ogimg.infoglobo.com.br/in/22131226-2b3-906/FT1086A/760/73400662_Brazil27s-Gremio-soccer-team-celebrates-winning-the-Copa-Libertadores-championship-after.jpg')
    
if __name__ == '__main__':
    dashboard()