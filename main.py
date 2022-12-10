"""
# Contoh aplikasi perhitungan ongkos cetakk
"""

import streamlit as st
import pandas as pd

# Judul APP
st.title ("Aplikasi perhitungan percetakan")

# Input parameter panjang dan lebar
lebar_bahan = st.number_input("Masukkan lebar bahan")
panjang = st.number_input("Masukkan panjang cm")
lebar = st.number_input("Masukkan lebar cm")
harga_bahan = st.number_input ("Masukkan harga bahan")
min_order = st.button ("Hitung minimum order")

if lebar > panjang :
    minimum = lebar_bahan / panjang
else :
    minimum = lebar_bahan / lebar

    st.write ("Minimum order =", minimum)

# Konversi cm ke m
fix_panjang = panjang / 10000
fix_lebar = lebar / 10000

# Hasil perhitungan
