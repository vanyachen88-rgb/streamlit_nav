import streamlit as st


pgnav = st.navigation (
      pages= ［"pages/home.py", "pages/mycv.py" , "pages/contactme.py","pages/myproject.py"］#把各個.py頁面放入這個參數
      position = "top"
)
