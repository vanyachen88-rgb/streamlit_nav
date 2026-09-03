import streamlit as st


pgnav = st.navigation (
      pages= ［"pages/home.py", "pages/mycv.py" , "pages/contactme.py","pages/myproject.py"］,
      position = "top"
)
pgnav.run()