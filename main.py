"""
# Contoh aplikasi perhitungan ongkos cetakk
"""

import streamlit as st
import pandas as pd

# Judul APP
st.title ("Aplikasi perhitungan percetakan")

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df
