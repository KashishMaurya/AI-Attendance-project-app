import streamlit as st


def style_background_home():
    st.markdown("""
        <style>

            /* =========================
               HOME BACKGROUND
            ========================= */

            .stApp {
                background: #0B1020 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background: #121A2F !important;
                padding: 2.5rem !important;
                border-radius: 1.5rem !important;

                border: 1px solid rgba(148, 163, 184, 0.12) !important;

                box-shadow:
                    0 20px 50px rgba(0, 0, 0, 0.25) !important;
            }

        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>

            /* =========================
               DASHBOARD BACKGROUND
            ========================= */

            .stApp {
                background: #0B1020 !important;
            }

        </style>
    """, unsafe_allow_html=True)


def style_base_layout():

    st.markdown("""
        <style>

        /* =========================
           FONTS
        ========================= */

        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Space+Grotesk:wght@300..700&display=swap');


        /* =========================
           STREAMLIT UI
        ========================= */

        #MainMenu,
        footer,
        header {
            visibility: hidden;
        }


        /* =========================
           MAIN CONTAINER
        ========================= */

        .block-container {
            padding-top: 1.5rem !important;
        }


        /* =========================
           HEADINGS
        ========================= */

        h1 {
            font-family: 'Space Grotesk', sans-serif !important;
            font-size: 3.5rem !important;
            font-weight: 700 !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;

            color: #F8FAFC !important;

            letter-spacing: -0.04em !important;
        }


        h2 {
            font-family: 'Space Grotesk', sans-serif !important;
            font-size: 2rem !important;
            font-weight: 650 !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;

            color: #F8FAFC !important;

            letter-spacing: -0.03em !important;
        }


        h3,
        h4,
        p {
            font-family: 'Inter', sans-serif !important;
        }


        h3,
        h4 {
            color: #E2E8F0 !important;
        }


        p {
            color: #3e454f;
        }


        /* =========================
           BUTTONS
        ========================= */

        button {
            border-radius: 0.75rem !important;

            background: #7C3AED !important;

            color: #FFFFFF !important;

            padding: 10px 20px !important;

            border: 1px solid rgba(255, 255, 255, 0.08) !important;

            font-family: 'Inter', sans-serif !important;

            font-weight: 600 !important;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                background 0.2s ease !important;
        }


        /* =========================
           SECONDARY BUTTON
        ========================= */

        button[kind="secondary"] {

            border-radius: 0.75rem !important;

            background: #06B6D4 !important;

            color: #06131A !important;

            padding: 10px 20px !important;

            border: none !important;

            font-family: 'Inter', sans-serif !important;

            font-weight: 600 !important;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                background 0.2s ease !important;
        }


        /* =========================
           TERTIARY BUTTON
        ========================= */

        button[kind="tertiary"] {

            border-radius: 0.75rem !important;

            background: #1E293B !important;

            color: #F8FAFC !important;

            padding: 10px 20px !important;

            border: 1px solid rgba(148, 163, 184, 0.15) !important;

            font-family: 'Inter', sans-serif !important;

            font-weight: 600 !important;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                background 0.2s ease !important;
        }


        /* =========================
           BUTTON HOVER
        ========================= */

        button:hover {
            transform: scale(1.03) !important;

            box-shadow:
                0 8px 25px rgba(124, 58, 237, 0.25) !important;
        }


        /* =========================
           INPUT FIELDS
        ========================= */

        input,
        textarea,
        [data-baseweb="select"] > div {

            background: #111827 !important;

            color: #F8FAFC !important;

            border: 1px solid #26334D !important;

            border-radius: 0.75rem !important;

            font-family: 'Inter', sans-serif !important;
        }


        input:focus,
        textarea:focus {

            border-color: #7C3AED !important;

            box-shadow:
                0 0 0 1px #7C3AED !important;
        }


        /* =========================
           LABELS
        ========================= */

        label {

            font-family: 'Inter', sans-serif !important;

            color: #CBD5E1 !important;

            font-weight: 500 !important;
        }


        /* =========================
           LINKS
        ========================= */

        a {

            color: #22D3EE !important;

            font-family: 'Inter', sans-serif !important;
        }


        a:hover {

            color: #67E8F9 !important;
        }

        </style>
    """, unsafe_allow_html=True)