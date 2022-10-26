import streamlit as st
import snowflake.connector as sc


@st.experimental_singleton(suppress_st_warning=True)

def init_connection():
    return sc.connect(**st.secrets["vbi"])

conn = init_connection()

@st.experimental_memo(ttl=600)

def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

st.balloons()
st.button('Click')
# run_query("Select * from CARTRIDGE_COMPARE_TEMP;")
