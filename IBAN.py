import string
import streamlit as st

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