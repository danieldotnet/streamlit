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


# Nicht in `if __name__ == '__main__':` wrappen
my_iban = st.chat_input("Set IBAN: ")

if my_iban:  # ✅ Null-Check
    my_iban = my_iban.replace(" ", "")

    if generate_iban_check_digits(my_iban) == my_iban[2:4] and valid_iban(my_iban):
        st.success('✅ IBAN ok!')
    else:
        st.error('❌ IBAN not ok!')