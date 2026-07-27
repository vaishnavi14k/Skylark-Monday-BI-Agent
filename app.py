import streamlit as st

from monday_client import (
    fetch_deals_board,
    fetch_work_orders_board
)

from data_cleaner import prepare_dataframe

from analytics import (
    revenue_summary,
    pipeline_health,
    sector_performance,
    deal_stage_summary,
    missing_data_report
)

from agent import generate_response


st.set_page_config(
    page_title="Skylark BI Agent",
    layout="wide"
)


st.title("🚁 Skylark Drones - Business Intelligence Agent")


# Fetch Monday Data

@st.cache_data
def load_data():

    deals_raw = fetch_deals_board()
    work_raw = fetch_work_orders_board()


    deals_df = prepare_dataframe(deals_raw)
    work_df = prepare_dataframe(work_raw)


    return deals_df, work_df



deals_df, work_df = load_data()



query = st.text_input(
    "Ask a business question"
)



if query:


    result = generate_response(
        query,
        deals_df,
        work_df
    )


    st.subheader("Business Insight")

    st.write(result)



with st.expander("Data Quality Report"):

    st.write(
        missing_data_report(deals_df)
    )