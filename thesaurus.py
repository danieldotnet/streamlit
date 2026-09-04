import requests
import streamlit as st

try:
    st.title('Thesaurus')

    term = st.text_input("Bitte Wort eingeben:")

    if st.button("Prüfen"):
        url = 'https://www.openthesaurus.de/synonyme/search?q=' + term + '&format=application/json'

        wjdata = requests.get(url).json()

        for i in wjdata["synsets"][0]["terms"]:
            st.write(i["term"])

except:
    pass