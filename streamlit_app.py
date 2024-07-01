import streamlit as st
from PyPDF2 import PdfMerger
import os

# Streamlit アプリの設定
st.title("PDF結合アプリ")

# ファイルアップロードウィジェット
uploaded_files = st.file_uploader("PDFファイルを選択してください", accept_multiple_files=True, type=["pdf"])

# PDFファイルがアップロードされたか確認
if uploaded_files:
    merger = PdfMerger()
    for uploaded_file in uploaded_files:
        # ファイルを一時保存
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        # Mergerに追加
        merger.append(uploaded_file.name)
    
    # 結合されたPDFを保存
    output_path = "merged.pdf"
    merger.write(output_path)
    merger.close()

    # 結合されたPDFのダウンロードリンクを表示
    with open(output_path, "rb") as f:
        st.download_button(
            label="結合されたPDFをダウンロード",
            data=f,
            file_name=output_path,
            mime="application/pdf"
        )
    
    # 一時ファイルを削除
    for uploaded_file in uploaded_files:
        os.remove(uploaded_file.name)
    os.remove(output_path)
