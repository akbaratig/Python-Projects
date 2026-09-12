import streamlit as st
from monty_hall import simulate_game, monty_hall_game
import time


st.title(":zap: Monty Hall Simulation...")
st.image("../images/monty_hall.png", width=400)
'------------------------------------'

number_of_game = st.number_input("Number of Simulations", min_value=1, max_value=10000, value=1000, step=1, key="num_simulations")
"-------------------------------------"

col1, col2 = st.columns(2)
col1.subheader("Win Percentage When Switching")
col2.subheader("Win Percentage When Not Switching")

chart_1 = col1.line_chart(x=None, y=None, height=300, width=400)
chart_2 = col2.line_chart(x=None, y=None, height=300, width=400)

wins_no_switching = 0
wins_switching = 0
for i in range(number_of_game):
    num_wins_with_switching, num_wins_without_switching = simulate_game(1)
    wins_switching += num_wins_with_switching
    wins_no_switching += num_wins_without_switching
    
    chart_1.add_rows([wins_no_switching / (i + 1)])
    chart_2.add_rows([wins_switching / (i + 1)])    
    
    time.sleep(0.01)  
