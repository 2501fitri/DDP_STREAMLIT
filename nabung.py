import streamlit as st

st.title("Ini Halaman dashboard!")

with st.form("nabung"):
    nama = st.text_input("Masukkan Nama")
    nominal = st.number_input("Masukkan nominal nabung")
    submitButton = st.form_submit_button("Simpan")

if submitButton:
    st.write(nama)
    st.session_stats['Nabung'].append({
        "nama": nama,
        "nominal": nominal,
    })
    st.succes("Berhasil Menabung!")