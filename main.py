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
def max_value(lebar,panjang,lebar_bahan):
    if lebar == 0 or panjang == 0 :
        return "input tidak valid, cek input nilai input anda!"
    else:
        min_order = lebar_bahan / max(lebar, panjang)
    return min_order

result = max_value(lebar, panjang, lebar_bahan)
st.write ("Minimum order =", result)


harga_bahan = st.number_input ("Masukkan harga bahan")
minimum_order = st.number_input ("Masukkan minimum order")

harga_order = (panjang * lebar)/10000 * minimum_order * harga_bahan
st.write ("Total harga=", harga_order)

#munculkan st.write saat ditekan tombol ya
