import streamlit as st
import pandas as pd
import joblib

model = joblib.load("iphone_price_model.pkl")
iphone_df = pd.read_csv("clean_iphone_data.csv")

st.set_page_config(
    page_title="iPhone Price Suggestor",
    page_icon="📱",
    layout="centered"
)

st.title("iPhone Price Suggestor")

st.write(
    "Estimate Bargain, Fair and Premium listing prices based on historical eBay listings."
)

model_name = st.selectbox(
    "Model",
    sorted(iphone_df["model"].unique())
)

storage = st.selectbox(
    "Storage",
    sorted(iphone_df["storage"].unique())
)

condition = st.selectbox(
    "Condition",
    sorted(iphone_df["condition"].unique())
)

carrier = st.selectbox(
    "Carrier",
    sorted(iphone_df["carrier"].unique())
)

if st.button("Suggest Price"):

    input_data = pd.DataFrame([{
        "model": model_name,
        "storage": storage,
        "condition": condition,
        "carrier": carrier
    }])

    fair_model_price = model.predict(input_data)[0]

    comparables = iphone_df[
        (iphone_df["model"] == model_name) &
        (iphone_df["storage"] == storage) &
        (iphone_df["condition"] == condition) &
        (iphone_df["carrier"] == carrier)
    ]

    if len(comparables) >= 5:
        bargain = comparables["Price"].quantile(0.20)
        fair = comparables["Price"].median()
        premium = comparables["Price"].quantile(0.80)
    else:
        bargain = fair_model_price * 0.90
        fair = fair_model_price
        premium = fair_model_price * 1.10

    st.subheader("Price Recommendation")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Bargain",
            f"${round(bargain)}"
        )

    with col2:
        st.metric(
            "Fair",
            f"${round(fair)}"
        )

    with col3:
        st.metric(
            "Premium",
            f"${round(premium)}"
        )

    st.caption(
        "*Based on historical eBay listing data collected in November 2023 in US."
    )
