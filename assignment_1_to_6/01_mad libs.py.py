import streamlit as st

st.set_page_config(page_title="Mad Libs Game", layout="centered")

st.title("🧠 Mad Libs Game")

with st.form("mad_libs_form"):
    adjective = st.text_input("Enter an adjective:")
    noun1 = st.text_input("Enter a noun:")
    verb_past_tense = st.text_input("Enter a verb (past tense):")
    adverb = st.text_input("Enter an adverb:")
    noun2 = st.text_input("Enter another noun:")
    exclamation = st.text_input("Enter an exclamation:")
    verb = st.text_input("Enter a verb:")
    noun3 = st.text_input("Enter one more noun:")

    submitted = st.form_submit_button("Generate Story")

if submitted:
    story = f"""
    {exclamation}! he said {adverb} as he jumped into his {adjective} {noun1}
    and {verb_past_tense} into the sunset. Later, he found a {noun2}
    and decided to {verb} it like a {noun3}.
    """
    st.subheader("Here's your story:")
    st.write(story)
