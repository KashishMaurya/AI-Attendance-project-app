import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):

    html = f"""
        <div style="
            background: #121A2F;
            padding: 22px 24px;
            border-radius: 16px;
            border: 1px solid #26334D;
            border-left: 4px solid #7C3AED;
            margin-bottom: 18px;

            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.18);
        ">

            <h3 style="
                margin: 0;
                color: #F8FAFC;
                font-size: 1.4rem;
                font-weight: 650;
                font-family: 'Inter', sans-serif;
            ">
                {name}
            </h3>

            <p style="
                color: #CBD5E1;
                margin: 10px 0 16px;
                font-size: 0.9rem;
                font-family: 'Inter', sans-serif;
            ">
                Code:
                <span style="
                    background: rgba(124, 58, 237, 0.15);
                    color: #A78BFA;
                    padding: 4px 9px;
                    border-radius: 6px;
                    font-weight: 600;
                    margin-left: 4px;
                ">
                    {code}
                </span>

                <span style="
                    color: #475569;
                    margin: 0 8px;
                ">
                    |
                </span>

                Section:
                <span style="
                    color: #E2E8F0;
                    font-weight: 500;
                ">
                    {section}
                </span>
            </p>
    """

    if stats:
        html += """
            <div style="
                display: flex;
                gap: 8px;
                flex-wrap: wrap;
                margin-top: 8px;
            ">
        """

        for icon, label, value in stats:

            html += f"""
                <div style="
                    background: #0F172A;
                    border: 1px solid #26334D;
                    padding: 7px 12px;
                    border-radius: 9px;

                    font-size: 0.85rem;
                    color: #94A3B8;

                    font-family: 'Inter', sans-serif;
                ">
                    <span style="margin-right: 3px;">
                        {icon}
                    </span>

                    <b style="
                        color: #F8FAFC;
                        font-weight: 600;
                    ">
                        {value}
                    </b>

                    <span style="margin-left: 3px;">
                        {label}
                    </span>
                </div>
            """

        html += "</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()