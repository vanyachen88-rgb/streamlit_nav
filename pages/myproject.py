import streamlit as st
st.title("專案首頁")


with st.sidebar:
    st.page_link("pages/home.py" , label="Home"),
    st.page_link("pages/mycv.py" , label="我的履歷"),
    st.page_link("pages/project1.py" , label="執行專案")