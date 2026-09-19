import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from hero import hero_banner
from theme import load_css

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
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
    "📊 Health Analytics Dashboard",
    "Visualize your wellness journey"
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
            "No health records found."
        )

        st.info(
            "Complete a Health Assessment first."
        )

        st.stop()

    latest = user_logs.iloc[-1]

    # -----------------------------
    # METRICS
    # -----------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "👤 User",
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

    with col4:
        st.metric(
            "📋 Assessments",
            len(user_logs)
        )

    st.markdown("---")

    # -----------------------------
    # LATEST HEALTH DATA
    # -----------------------------

    st.subheader("📊 Latest Health Summary")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Sleep",
            latest["sleep_hours"]
        )

    with c2:
        st.metric(
            "Water",
            latest["water_intake"]
        )

    with c3:
        st.metric(
            "Exercise",
            latest["exercise_minutes"]
        )

    with c4:
        st.metric(
            "Stress",
            latest["stress_level"]
        )

    st.markdown("---")

    # -----------------------------
    # HEALTH SCORE TREND
    # -----------------------------

    st.subheader("📈 Health Score Trend")

    fig1, ax1 = plt.subplots()

    ax1.plot(
        user_logs["id"],
        user_logs["health_score"],
        marker="o"
    )

    ax1.set_xlabel("Assessment")
    ax1.set_ylabel("Health Score")
    ax1.set_title("Health Score Progress")

    st.pyplot(fig1)

    st.markdown("---")

    # -----------------------------
    # STRESS LEVEL TREND
    # -----------------------------

    st.subheader("🧘 Stress Level Trend")

    fig2, ax2 = plt.subplots()

    ax2.plot(
        user_logs["id"],
        user_logs["stress_level"],
        marker="o"
    )

    ax2.set_xlabel("Assessment")
    ax2.set_ylabel("Stress Level")
    ax2.set_title("Stress Trend")

    st.pyplot(fig2)

    st.markdown("---")

    # -----------------------------
    # HISTORY TABLE
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
        f"Database Error: {e}"
    )