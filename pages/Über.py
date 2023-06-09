# =============================================================================
# -----------------------Leukofit APP-------------------
#   Beschreibung: Das ist die "Über"-Seite
#   Hier werden die Informationen zu den Entwicklerinnen dargestellt. 
#   
#    Datum: 12.04.2023
#    Autoren: Gzime Ramadani, Rinesa Shabija, Priya Jose
# =============================================================================



# Schritt 1: Erstellen der Multipage APP=======================================
#   Es wird eine Multipage APP erstellt.
#   Es wird der Seitentitel mit Icon definiert.
#   Es werden die Bilbiotheken / Packages importiert.
# =============================================================================

import streamlit as st
st.set_page_config(
    page_title="Über",
    page_icon="💓",
)

# Titel und Header
st.title ("Über diese APP")
st.header("Leukorechner")


# Schritt 2: Informationen zu den Entwicklerinnen==============================
#   Hier werden die Informationen sowie ein Bild eingefügt
# =============================================================================

# Informationen und Bild
st.subheader('Version: 1.0')
st.subheader('Datum: 10.04.2023')
st.subheader('Entwickler: Gzime Ramadani, Rinesa Shabija, Priya Jose')
st.subheader('Im Auftrag der Zürcher Hochschule für angewandte Wissenschaften')
from PIL import Image
image = Image.open('media\zhaw.png')
st.image(image, caption='Copyright ZHAW')