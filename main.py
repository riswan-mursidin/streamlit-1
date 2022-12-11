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

# Mencari minimum order
def max_value(lebar,panjang,lebar_bahan):
    if lebar == 0 or panjang == 0 :
        return "0"
    else:
        min_order = lebar_bahan / max(lebar, panjang)
    return min_order

result = max_value(lebar, panjang, lebar_bahan)
minimum = st.button ("Minimum Order")
st.write ("Minimum order =", result)


harga_bahan = st.number_input ("Masukkan harga bahan per meter")
minimum_order = st.number_input ("Masukkan minimum order")

harga_orderfix =  ((panjang * lebar)/10000 * minimum_order * harga_bahan)

harga_order = st.button ("Total Harga")

st.write ("Total harga=", harga_orderfix)


#munculkan st.write saat ditekan tombol ya
