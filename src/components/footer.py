import streamlit as st

def footer_home():
    st.markdown(
        """
        <div class="footer">
            <span>© 2026</span>
            <span class="dot">•</span>
            <strong>Kashish Maurya</strong>
        </div>

        <style>
        .footer {
            position: fixed;
            right: 22px;
            bottom: 14px;
            z-index: 9999;

            display: flex;
            align-items: center;
            gap: 7px;

            font-size: 11px;
            letter-spacing: 0.3px;
            color: white;
        }

        .footer strong {
            color: yellow;
            font-weight: 600;
        }

        .footer .dot {
            opacity: 0.5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def footer_dashboard():
    st.markdown(
        """
        <div class="footer">
            <span>© 2026</span>
            <span class="dot">•</span>
            <strong>Kashish Maurya</strong>
        </div>

        <style>
        .footer {
            position: fixed;
            right: 22px;
            bottom: 14px;
            z-index: 9999;

            display: flex;
            align-items: center;
            gap: 7px;

            font-size: 11px;
            letter-spacing: 0.3px;
            color: white;
        }

        .footer strong {
            color: yellow;
            font-weight: 600;
        }

        .footer .dot {
            opacity: 0.5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )