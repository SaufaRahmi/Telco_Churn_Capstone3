import streamlit as st
import pandas as pd

def show_history():
    st.title("Prediction History")
    if 'predicthistory' in st.session_state and st.session_state.predicthistory:
        history_df = pd.DataFrame(st.session_state.predicthistory)
        st.write(history_df)
    else:
        st.write("No predictions made yet.")
