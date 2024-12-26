import streamlit as st

streamlit

st.write('Hello World!')

dashboard = st.page("./pages/dashboard.py", "title=dashboard")
nabung = st.page("./pages/nabung.py", "title=nabung")

pg = st.navigation
({
        "Dashboard": [dashboard],
        "Nabung": [nabung],    
})

if "Nabung" not in st.session_stats:
    st.session_stats["Nabung"] = []

pg.run()