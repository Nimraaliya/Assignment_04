import streamlit as st
import random

st.set_page_config(page_title="Rock Paper Scissors", layout="centered")

st.title("✊✋✌️ Rock, Paper, Scissors")

choices = ["rock", "paper", "scissors"]
user_choice = st.radio("Choose your move:", choices, index=0)

if st.button("Play"):
    computer_choice = random.choice(choices)

    st.write(f"🤖 Computer chose: **{computer_choice}**")
    
    if user_choice == computer_choice:
        st.info("🤝 It's a Tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        st.success("🎉 You win!")
    else:
        st.error("😞 You lose!")

