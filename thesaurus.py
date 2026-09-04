import requests
import streamlit as st

try:
    term = st.text_input("Bitte Wort eingeben:")
    url = 'https://www.openthesaurus.de/synonyme/search?q=' + term + '&format=application/json'

    wjdata = requests.get(url).json()

    st.title('Thesaurus')

    for i in wjdata["synsets"][0]["terms"]:
        st.write(i["term"])
    print('')

except:
    pass