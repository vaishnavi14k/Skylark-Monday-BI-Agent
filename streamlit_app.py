import streamlit as st

from monday_client import (
    fetch_deals_board,
    fetch_work_orders_board
)

from data_cleaner import prepare_dataframe

from agent import generate_response



st.title(
    "🚁 Skylark Drones BI Agent"
)



@st.cache_data
def load_data():

    deals_raw = fetch_deals_board()

    work_raw = fetch_work_orders_board()


    deals_df = prepare_dataframe(
        deals_raw
    )

    work_df = prepare_dataframe(
        work_raw
    )


    return deals_df, work_df



deals_df, work_df = load_data()



question = st.text_input(
    "Ask a business question"
)



if question:

    answer = generate_response(
        question,
        deals_df,
        work_df
    )


    st.write(answer)