import streamlit as st

from predict import predict_fraud


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CreditGuard - Fraud Detection",
    page_icon="💳",
    layout="wide"
)


# ============================================================
# CENTER THE APPLICATION
# ============================================================

left_space, main_area, right_space = st.columns(
    [1, 8, 1]
)


with main_area:

    # ========================================================
    # HEADER
    # ========================================================

    st.title("💳 CreditGuard")

    st.subheader("AI-Powered Credit Card Fraud Detection")

    st.write(
        "Analyze transaction patterns and identify potentially "
        "fraudulent transactions using Machine Learning."
    )

    st.divider()


    # ========================================================
    # SMART FRAUD DETECTION
    # ========================================================

    st.header("🛡️ Smart Fraud Detection")

    col1, col2, col3 = st.columns(3)

    with col1:

        with st.container(border=True):

            st.subheader("🤖 Random Forest")

            st.write(
                "Uses multiple decision trees to identify "
                "patterns associated with fraudulent "
                "transactions."
            )


    with col2:

        with st.container(border=True):

            st.subheader("📊 Binary Classification")

            st.write(
                "Classifies transactions as legitimate or "
                "potentially fraudulent."
            )


    with col3:

        with st.container(border=True):

            st.subheader("🛡️ Fraud Probability")

            st.write(
                "Provides a probability score to understand "
                "the model's prediction."
            )


    st.divider()


    # ========================================================
    # TRANSACTION ANALYSIS
    # ========================================================

    st.header("🔍 Transaction Analysis")

    st.write(
        "Enter the transaction details below and analyze "
        "the transaction using the trained Machine Learning model."
    )


    col1, col2 = st.columns(2)


    with col1:

        time = st.number_input(
            "⏱️ Transaction Time",
            min_value=0.0,
            value=0.0,
            help="Time elapsed since the first transaction."
        )


    with col2:

        amount = st.number_input(
            "💰 Transaction Amount",
            min_value=0.0,
            value=100.0,
            step=1.0,
            help="Enter the transaction amount."
        )


    # ========================================================
    # ADVANCED FEATURES
    # ========================================================

    with st.expander("⚙️ Advanced Features (V1–V28)"):

        st.info(
            "V1–V28 are anonymized numerical features from the "
            "dataset. Their individual real-world meanings are "
            "not provided. The trained model uses these features "
            "to identify transaction patterns."
        )

        values = {}

        feature_columns = st.columns(4)

        for i in range(1, 29):

            with feature_columns[(i - 1) % 4]:

                values[f"V{i}"] = st.number_input(
                    f"V{i}",
                    value=0.0,
                    format="%.6f"
                )


    st.write("")


    # ========================================================
    # ANALYZE BUTTON
    # ========================================================

    button_left, button_center, button_right = st.columns(
        [1, 2, 1]
    )


    with button_center:

        analyze = st.button(
            "🔎 Analyze Transaction",
            type="primary",
            use_container_width=True
        )


    # ========================================================
    # PREDICTION
    # ========================================================

    if analyze:

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


            st.divider()

            st.header("📊 Analysis Result")


            # ------------------------------------------------
            # PREDICTION RESULT
            # ------------------------------------------------

            if prediction == 0:

                st.success(
                    "✅ Transaction Appears Legitimate"
                )

                st.write(
                    "The trained model classified this "
                    "transaction as legitimate."
                )


            else:

                st.error(
                    "🚨 Potential Fraud Detected"
                )

                st.write(
                    "The trained model classified this "
                    "transaction as potentially fraudulent."
                )


            # ------------------------------------------------
            # PROBABILITY
            # ------------------------------------------------

            st.subheader("Fraud Probability")

            result_col1, result_col2 = st.columns(2)


            with result_col1:

                st.metric(
                    "Fraud Probability",
                    f"{probability_percent:.2f}%"
                )


            with result_col2:

                st.metric(
                    "Classification",
                    "Fraud" if prediction == 1
                    else "Legitimate"
                )


            st.progress(float(probability))


            st.caption(
                "This probability represents the model's "
                "estimated likelihood that the transaction "
                "is fraudulent."
            )


            # ------------------------------------------------
            # MODEL INFORMATION
            # ------------------------------------------------

            st.divider()

            st.subheader("🤖 Model Information")

            model_col1, model_col2, model_col3 = st.columns(3)


            with model_col1:

                st.metric(
                    "Algorithm",
                    "Random Forest"
                )


            with model_col2:

                st.metric(
                    "Task",
                    "Binary Classification"
                )


            with model_col3:

                st.metric(
                    "Input Features",
                    "30"
                )


            st.caption(
                "Prediction generated using the trained "
                "Random Forest model and the selected "
                "classification threshold."
            )


        except Exception as e:

            st.error(
                f"Prediction error: {e}"
            )


    # ========================================================
    # HOW CREDITGUARD WORKS
    # ========================================================

    st.divider()

    with st.expander("💡 How CreditGuard Works"):

        st.subheader("1️⃣ Enter Transaction Details")

        st.write(
            "Enter the transaction amount and time. "
            "Additional anonymized features can be entered "
            "under Advanced Features."
        )


        st.subheader("2️⃣ Machine Learning Analysis")

        st.write(
            "The Random Forest model analyzes the transaction "
            "features and identifies learned patterns."
        )


        st.subheader("3️⃣ Get the Prediction")

        st.write(
            "The system displays the fraud probability "
            "and classifies the transaction."
        )


    # ========================================================
    # PROJECT INFORMATION
    # ========================================================

    st.divider()

    st.header("📌 Project Information")

    info_col1, info_col2, info_col3 = st.columns(3)


    with info_col1:

        st.write("**Domain**")

        st.write("Machine Learning")


    with info_col2:

        st.write("**Model**")

        st.write("Random Forest")


    with info_col3:

        st.write("**Interface**")

        st.write("Streamlit")


    # ========================================================
    # FOOTER
    # ========================================================

    st.divider()

    st.caption(
        "💳 CreditGuard | Credit Card Fraud Detection"
    )

    st.caption(
        "Machine Learning • Random Forest • Streamlit"
    )

    st.caption(
        "Academic project. Predictions should not be treated "
        "as final financial or banking decisions."
    )