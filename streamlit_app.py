import string
import streamlit as st

# Custom CSS, um das GitHub-Icon auszublenden
hide_github_icon = """
    <style>
    #GithubIcon {
        visibility: hidden;
    }
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK {
        display: none !important;
    }
    </style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}


def _number_iban(iban):
    return (iban[4:] + iban[:4]).translate(LETTERS)


def generate_iban_check_digits(iban):
    number_iban = _number_iban(iban[:2] + '00' + iban[4:])
    return '{:0>2}'.format(98 - (int(number_iban) % 97))


def valid_iban(iban):
    return int(_number_iban(iban)) % 97 == 1


st.title("IBAN Validator")

iban_input = st.text_input("IBAN eingeben:")

if st.button("Prüfen"):
    if not iban_input:
        st.warning("Bitte IBAN eingeben")
    else:
        iban = iban_input.replace(" ", "").upper()

        if len(iban) < 15:
            st.error(f"IBAN zu kurz ({len(iban)} Zeichen)")
        else:
            try:
                check = generate_iban_check_digits(iban)
                if check == iban[2:4] and valid_iban(iban):
                    st.success("✅ IBAN gültig!")
                else:
                    st.error("❌ IBAN ungültig")
            except:
                st.error("❌ Format-Fehler")