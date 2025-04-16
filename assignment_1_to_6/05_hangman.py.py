import streamlit as st
import random

st.set_page_config(page_title="Hangman Game", layout="centered")
st.title("🪢 Hangman Game")

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = random.choice(['python', 'hangman', 'streamlit', 'challenge', 'programming'])
    st.session_state.guesses = []
    st.session_state.attempts = 12
    st.session_state.game_over = False

def display_current_word():
    return ' '.join([letter if letter in st.session_state.guesses else '_' for letter in st.session_state.word])

# Game display
st.subheader("Guess the word:")
st.write(display_current_word())
st.write(f"🔁 Attempts left: {st.session_state.attempts}")

# Guess input
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter:", max_chars=1).lower()

    if st.button("Guess"):
        if not guess.isalpha():
            st.warning("Please enter a valid letter.")
        elif guess in st.session_state.guesses:
            st.info("You've already guessed that letter.")
        else:
            st.session_state.guesses.append(guess)

            if guess not in st.session_state.word:
                st.session_state.attempts -= 1

        # Check for win/loss
        if all(letter in st.session_state.guesses for letter in st.session_state.word):
            st.success(f"🎉 You guessed it! The word was **{st.session_state.word}**.")
            st.session_state.game_over = True
        elif st.session_state.attempts == 0:
            st.error(f"💀 Game Over! The word was **{st.session_state.word}**.")
            st.session_state.game_over = True

# Reset button
if st.button("🔄 Play Again"):
    st.session_state.word = random.choice(['python', 'hangman', 'streamlit', 'challenge', 'programming'])
    st.session_state.guesses = []
    st.session_state.attempts = 12
    st.session_state.game_over = False
