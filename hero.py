import streamlit as st

def hero_banner(title, subtitle):
    st.markdown(
        f"""
        <div style="
        padding:30px;
        border-radius:20px;
        background:linear-gradient(90deg,#9333ea,#c084fc);
        text-align:center;
        color:white;
        margin-bottom:30px;
        ">
            <h1>{title}</h1>
            <h4>{subtitle}</h4>
        </div>
        """,
        unsafe_allow_html=True
    )