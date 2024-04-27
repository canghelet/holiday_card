from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain


# Directories and file paths

THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "Animation - 1713640040365.json"


# Load and display the animation

def load_lottie_animation(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


# Function to apply effect

def run_rain_animation():
    rain(emoji ="🐰", font_size = 20, falling_speed = 5, animation_length='infinite')


# Function to get the name from the query parameters

def get_person_name():
    query_params = st._get_query_params()
    return query_params.get("nume", ["Prieten"])[0]

# Page configuration

st.set_page_config(page_title="Paste Fericit", page_icon="🐰")


#Run rain animation

run_rain_animation()


# Apply CSS

with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)


# Display name with personalized name

PERSON_NAME = get_person_name()
st.header(f"Paste Fericit, {PERSON_NAME}! 🐰", anchor=False)


# Display lottie animation

lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=400)


# Personalized message

st.markdown(
    f"Draga {PERSON_NAME}, iti doresc ca bucuria Invierii Domnului sa iti lumineze sufletul si sa iti ofere in dar armonie, liniste sufleteasca si bucurie!\n"
    f"Cu lumanarile aprinse, sa ne bucuram impreuna ca Hristos a Inviat!🎇\n\n"
    f"Sa ai parte de sarbatori binecuvantate, bucate gustoase si momente magice in compania celor dragi!🌈"
)



