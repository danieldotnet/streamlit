import string
import streamlit as st

LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}


def _number_iban(iban):
    return (iban[4:] + iban[:4]).translate(LETTERS)


def generate_iban_check_digits(iban):
    try:
        if len(iban) < 4:
            return None
        number_iban = _number_iban(iban[:2] + '00' + iban[4:])
        return '{:0>2}'.format(98 - (int(number_iban) % 97))
    except ValueError:
        return None


def valid_iban(iban):
    try:
        if len(iban) < 15:
            return False
        return int(_number_iban(iban)) % 97 == 1
    except (ValueError, IndexError, KeyError):
        return False


st.title("IBAN Validator")

my_iban = st.chat_input("Set IBAN: ")

if my_iban:
    my_iban = my_iban.replace(" ", "").upper()

    if len(my_iban) < 15:
        st.error(f"❌ IBAN zu kurz (mind. 15 Zeichen, hast {len(my_iban)})")
    else:
        check_digits = generate_iban_check_digits(my_iban)
        is_valid = valid_iban(my_iban)

        if check_digits and check_digits == my_iban[2:4] and is_valid:
            st.success('✅ IBAN ok!')
        else:
            st.error('❌ IBAN not ok!')