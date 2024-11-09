import streamlit as st

# Import each section module
from basic_profile import basic_profile_section
from diamond_character import diamond_character_section
from character_evaluation import character_evaluation_section
from biblical_mirror import biblical_mirror_section
from fruits_spoils import fruits_spoils_section
from inner_light import inner_light_section

# Title and Description
st.title("Digital Character Workbook")
st.markdown("Welcome to the Digital Character Workbook. Follow each section to develop your character in depth.")

# Display each section in sequence
st.header("Basic Profile")
basic_profile_section()

st.header("Diamond of Human Character")
diamond_character_section()

st.header("Character Evaluation")
character_evaluation_section()

st.header("Biblical Mirror")
biblical_mirror_section()

st.header("Fruits and Spoils")
fruits_spoils_section()

st.header("The Inner Light")
inner_light_section()

# Placeholder for author webpage link
st.markdown("---")
st.markdown("Visit my [author webpage](#) for more information.")  # Update the link once the webpage is ready
