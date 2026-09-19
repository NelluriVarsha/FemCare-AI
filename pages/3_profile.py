import streamlit as st
import sqlite3
import pandas as pd

from hero import hero_banner
from theme import load_css

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
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
    "👤 My Health Profile",
    "Your personal wellness dashboard"
)

# -----------------------------
# LOGIN CHECK
# -----------------------------

if "username" not in st.session_state:

    st.warning(
        "Please login first."
    )

    st.stop()

username = st.session_state["username"]

# -----------------------------
# DATABASE
# -----------------------------

try:

    conn = sqlite3.connect("users.db")

    user_logs = pd.read_sql_query(
        """
        SELECT * FROM health_logs
        WHERE username = ?
        """,
        conn,
        params=(username,)
    )

    conn.close()

    if len(user_logs) == 0:

        st.warning(
            "No health records found for this user."
        )

        st.info(
            "Complete a Health Assessment first."
        )

        st.stop()

    latest = user_logs.iloc[-1]

    # -----------------------------
    # PROFILE CARDS
    # -----------------------------

    st.subheader("💜 Health Profile")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "👤 Username",
            username
        )

    with col2:
        st.metric(
            "💜 Health Score",
            latest["health_score"]
        )

    with col3:
        st.metric(
            "🌸 PCOS Risk",
            latest["pcos_risk"]
        )

    st.markdown("---")

    # -----------------------------
    # HEALTH SUMMARY
    # -----------------------------

    left, right = st.columns([2, 1])

    with left:

        st.subheader("📊 Latest Assessment")

        st.success(
            f"😴 Sleep Hours : {latest['sleep_hours']}"
        )

        st.success(
            f"💧 Water Intake : {latest['water_intake']} L"
        )

        st.success(
            f"🏃 Exercise Minutes : {latest['exercise_minutes']}"
        )

        st.success(
            f"🧘 Stress Level : {latest['stress_level']}"
        )

        st.info(
            f"📝 Symptoms : {latest['symptoms']}"
        )

    with right:

        st.info("""
### 🌸 Wellness Goals

💧 Drink 2-3 Liters Water

😴 Sleep 7-8 Hours

🏃 Exercise Daily

🧘 Reduce Stress

🥗 Healthy Nutrition
""")

    st.markdown("---")

    # -----------------------------
    # HEALTH STATUS
    # -----------------------------

    st.subheader("📈 Health Status")

    score = latest["health_score"]

    if score >= 80:

        st.success(
            "Excellent Health Status ✅"
        )

    elif score >= 60:

        st.info(
            "Good Health Status 👍"
        )

    else:

        st.warning(
            "Needs Improvement ⚠️"
        )

    st.markdown("---")

    # -----------------------------
    # ASSESSMENT HISTORY
    # -----------------------------

    st.subheader("📋 Assessment History")

    st.dataframe(
        user_logs.sort_values(
            by="id",
            ascending=False
        ),
        use_container_width=True
    )

except Exception as e:

    st.error(
        f"Error : {e}"
    )