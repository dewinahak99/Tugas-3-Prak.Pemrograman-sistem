import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.title("Visualisasi Dataset dengan 5 Kolom Terpisah")

# Memungkinkan pengguna untuk mengunggah dataset mereka
uploaded_file = st.file_uploader("Unggah dataset CSV Anda", type=["csv"])

# Jika file diunggah, baca dan tampilkan datanya
if uploaded_file is not None:
    # Membaca dataset yang diunggah
    data = pd.read_csv(uploaded_file)

    # Menampilkan dataset
    st.write("Dataset yang diunggah:")
    st.dataframe(data)

    # Memilih lima kolom yang akan divisualisasikan
    st.write("Pilih lima kolom untuk divisualisasikan:")
    selected_columns = st.multiselect("Pilih lima kolom", data.columns, default=data.columns[:5], max_selections=5)

    # Jika pengguna sudah memilih lima kolom
    if len(selected_columns) == 5:
        st.write(f"Menampilkan grafik untuk kolom: {', '.join(selected_columns)}")
        
        # Menampilkan grafik line chart untuk setiap kolom yang dipilih, dipisahkan dengan jelas
        for column in selected_columns:
            st.subheader(f"Grafik untuk kolom: {column}")
            st.line_chart(data[[column]])
            st.write("---")  # Menambahkan garis pemisah antar grafik
    else:
        st.write("Silakan pilih tepat lima kolom untuk divisualisasikan.")
else:
    st.write("Silakan unggah file CSV untuk memulai.")
