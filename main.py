"""
# Contoh aplikasi perhitungan ongkos cetakk
"""

import streamlit as st

# Judul APP
st.title ("Aplikasi perhitungan percetakan")

# Input parameter panjang dan lebar
lebar_bahan = st.number_input("Masukkan lebar bahan")
panjang = st.number_input("Masukkan panjang cm")
lebar = st.number_input("Masukkan lebar cm")
min_order = st.button ("Hitung minimum order")

# Mencari minimum order
if lebar > panjang :
    min_order = lebar_bahan / panjang
else :
    min_order = lebar_bahan / lebar

    st.write ("Minimum order =", min_order)


harga_bahan = st.number_input ("Masukkan harga bahan")


# Konversi cm ke m
fix_panjang = panjang / 10000
fix_lebar = lebar / 10000

# Hasil perhitungan
