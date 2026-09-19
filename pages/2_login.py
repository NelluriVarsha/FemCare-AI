import streamlit as st
import sqlite3

from hero import hero_banner
from theme import load_css

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="FemCare Login",
    page_icon="🔐",
    layout="wide"
)

load_css()

# -----------------------------
# BACK BUTTON
# -----------------------------

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

# -----------------------------
# HERO SECTION
# -----------------------------

hero_banner(
    "💜 Welcome Back",
    "Continue your wellness journey with FemCare AI"
)

# -----------------------------
# TWO COLUMN LAYOUT
# -----------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("🔐 Login Form")

    username = st.text_input(
        "Username"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "💜 Login",
        use_container_width=True
    ):

        if username == "" or password == "":

            st.warning(
                "Please Enter Username and Password"
            )

        else:

            try:

                conn = sqlite3.connect(
                    "users.db"
                )

                cursor = conn.cursor()

                cursor.execute(
                    """
                    SELECT * FROM accounts
                    WHERE username=? AND password=?
                    """,
                    (
                        username,
                        password
                    )
                )

                user = cursor.fetchone()

                conn.close()

                if user:

                    # Save logged-in user
                    st.session_state["username"] = username

                    st.success(
                        "Login Successful ✅"
                    )

                    st.balloons()

                    st.success(
                        f"Welcome, {username} 💜"
                    )

                    # Redirect to Profile
                    st.switch_page(
                        "pages/3_profile.py"
                    )

                else:

                    st.error(
                        "Invalid Username or Password ❌"
                    )

            except Exception as e:

                st.error(
                    f"Database Error: {e}"
                )

with right:

    st.info(
        """
### 💜 Why Login?

✅ Access Dashboard

✅ View Reports

✅ Track Health Progress

✅ Monitor PCOS Risk

✅ Personalized Recommendations

✅ Wellness Analytics
"""
    )

    st.success(
        """
🌸 FemCare Benefits

Track daily health

Monitor wellness trends

Receive AI recommendations

Manage your health journey
"""
    )