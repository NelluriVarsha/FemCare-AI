import streamlit as st
import sqlite3
from datetime import datetime, timedelta

from hero import hero_banner
from theme import load_css

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Menstrual Tracker",
    page_icon="🌸",
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
    "🌸 Menstrual Cycle Tracker",
    "Track periods, ovulation and cycle health"
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
# INPUT SECTION
# -----------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("📅 Menstrual Information")

    last_period = st.date_input(
        "Last Period Start Date"
    )

    cycle_length = st.number_input(
        "Average Cycle Length (Days)",
        min_value=21,
        max_value=60,
        value=28
    )

    period_duration = st.number_input(
        "Period Duration (Days)",
        min_value=1,
        max_value=15,
        value=5
    )

    cycle_type = st.selectbox(
        "Cycle Type",
        [
            "Regular",
            "Irregular"
        ]
    )

    st.subheader("🌸 Symptoms")

    cramps = st.checkbox("Cramps")

    acne = st.checkbox("Acne")

    mood_swings = st.checkbox("Mood Swings")

    headache = st.checkbox("Headache")

    fatigue = st.checkbox("Fatigue")

    bloating = st.checkbox("Bloating")

with right:

    st.info("""
### 🌸 Healthy Cycle Tips

✅ Track periods regularly

✅ Drink enough water

✅ Maintain healthy weight

✅ Exercise regularly

✅ Sleep 7-8 hours

✅ Reduce stress
""")

# -----------------------------
# ANALYZE
# -----------------------------

if st.button(
    "🌸 Analyze Cycle",
    use_container_width=True
):

    next_period = (
        last_period +
        timedelta(days=cycle_length)
    )

    ovulation_day = (
        next_period -
        timedelta(days=14)
    )

    fertile_start = (
        ovulation_day -
        timedelta(days=5)
    )

    fertile_end = (
        ovulation_day +
        timedelta(days=1)
    )

    # -------------------------
    # SAVE TO DATABASE
    # -------------------------

    try:

        conn = sqlite3.connect(
            "users.db"
        )

        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS menstrual_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            last_period_date TEXT,
            cycle_length INTEGER,
            period_duration INTEGER,
            cycle_type TEXT
        )
        """)

        cursor.execute(
            """
            INSERT INTO menstrual_logs
            (
                username,
                last_period_date,
                cycle_length,
                period_duration,
                cycle_type
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                username,
                str(last_period),
                cycle_length,
                period_duration,
                cycle_type
            )
        )

        conn.commit()
        conn.close()

    except Exception as e:

        st.error(
            f"Database Error: {e}"
        )

    # -------------------------
    # RESULTS
    # -------------------------

    st.success(
        "Cycle Information Saved Successfully ✅"
    )

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "📅 Next Period",
            next_period.strftime(
                "%d-%b-%Y"
            )
        )

    with c2:

        st.metric(
            "🥚 Ovulation Day",
            ovulation_day.strftime(
                "%d-%b-%Y"
            )
        )

    with c3:

        st.metric(
            "🌸 Cycle Type",
            cycle_type
        )

    st.markdown("---")

    st.subheader(
        "💡 Fertility Window"
    )

    st.info(
        f"""
Fertile Window:

{fertile_start.strftime('%d-%b-%Y')}
to
{fertile_end.strftime('%d-%b-%Y')}
"""
    )

    st.markdown("---")

    st.subheader(
        "🤖 FemCare AI Insights"
    )

    if cycle_length > 35:

        st.warning("""
⚠ Your cycle appears longer than normal.

This may indicate hormonal imbalance
or PCOS-related symptoms.

Consider consulting a healthcare professional.
""")

    elif cycle_length < 21:

        st.warning("""
⚠ Your cycle appears shorter than normal.

Monitor your cycle regularly.
""")

    else:

        st.success("""
✅ Your cycle length appears healthy.
""")