import streamlit as st
import sqlite3

from hero import hero_banner

st.set_page_config(
    page_title="FemCare Register",
    page_icon="🌸",
    layout="wide"
)
from theme import load_css

load_css()

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

hero_banner(
    "🌸 Join FemCare AI",
    "Create your personalized women's wellness account"
)

left, right = st.columns([2, 1])

with left:

    st.subheader("📝 Registration Form")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button(
        "💜 Create Account",
        use_container_width=True
    ):

        if username == "" or password == "":
            st.warning("Please fill all fields")

        elif password != confirm_password:
            st.error("Passwords do not match ❌")

        else:

            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            try:

                cursor.execute(
                    """
                    INSERT INTO accounts
                    (username,password)
                    VALUES (?,?)
                    """,
                    (username, password)
                )

                conn.commit()

                st.success(
                    "Registration Successful ✅"
                )

            except sqlite3.IntegrityError:

                st.error(
                    "Username already exists ❌"
                )

            conn.close()

with right:

    st.info(
        """
        🌸 Benefits

        ✅ Health Tracking

        ✅ PCOS Risk Assessment

        ✅ AI Recommendations

        ✅ Wellness Dashboard

        ✅ Download Reports
        """
    )