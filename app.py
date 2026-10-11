import streamlit as st
import pandas as pd

from predict import predict_fraud


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)


# -----------------------------
# Header
# -----------------------------
st.title("💳 Credit Card Fraud Detection")
st.markdown(
    "### AI-powered transaction analysis using Machine Learning"
)

st.info(
    "Enter the transaction details below and click **Check Transaction** "
    "to predict whether the transaction is legitimate or potentially fraudulent."
)

st.divider()


# -----------------------------
# Transaction Input
# -----------------------------
st.subheader("🔍 Transaction Details")

st.write(
    "The model uses 30 numerical features from the credit card transaction dataset."
)

col1, col2 = st.columns(2)

with col1:
    time = st.number_input(
        "Transaction Time",
        min_value=0.0,
        value=0.0
    )

with col2:
    amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=100.0
    )


# -----------------------------
# Advanced Features
# -----------------------------
with st.expander("⚙️ Advanced Transaction Features (V1–V28)"):

    st.caption(
        "V1–V28 are anonymized numerical features provided by the dataset."
    )

    values = {}

    cols = st.columns(4)

    for i in range(1, 29):
        with cols[(i - 1) % 4]:
            values[f"V{i}"] = st.number_input(
                f"V{i}",
                value=0.0,
                format="%.6f"
            )


st.divider()


# -----------------------------
# Prediction
# -----------------------------
if st.button(
    "🔎 Check Transaction",
    type="primary",
    use_container_width=True
):

    transaction_data = {
        "Time": time
    }

    for i in range(1, 29):
        transaction_data[f"V{i}"] = values[f"V{i}"]

    transaction_data["Amount"] = amount

    try:

        prediction, probability = predict_fraud(
            list(transaction_data.values())
        )

        probability_percent = probability * 100

        st.subheader("📊 Prediction Result")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                "Fraud Probability",
                f"{probability_percent:.2f}%"
            )

        with result_col2:
            if prediction == 1:
                st.error("🚨 Potential Fraudulent Transaction")
            else:
                st.success("✅ Legitimate Transaction")

        st.progress(float(probability))

        st.caption(
            "The prediction is based on the trained Random Forest model "
            "and the selected classification threshold."
        )

    except Exception as e:
        st.error(f"Prediction error: {e}")


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Credit Card Fraud Detection | Machine Learning + Streamlit"
)