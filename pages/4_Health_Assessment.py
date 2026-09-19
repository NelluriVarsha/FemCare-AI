import streamlit as st
import sqlite3

from health_score import calculate_health_score
from pcos_predictor import predict_pcos
from recommendation import get_recommendations
from theme import load_css

load_css()
# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Health Assessment",
    page_icon="💜",
    layout="wide"
)

# -----------------------------
# BACK BUTTON
# -----------------------------

if st.button("⬅ Back to Home"):
    st.switch_page("app.py")

# -----------------------------
# HERO BANNER
# -----------------------------

st.markdown("""
<div style="
padding:25px;
border-radius:15px;
background:linear-gradient(90deg,#9333ea,#c084fc);
text-align:center;
color:white;
margin-bottom:20px;
">
<h1>💜 Women's Wellness Assessment</h1>
<p>Track health habits and assess PCOS risk</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# MAIN LAYOUT
# -----------------------------

left, right = st.columns([2, 1])

with left:

    st.subheader("💜 Daily Health Tracking")

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0.0,
        max_value=24.0,
        step=0.5
    )

    water_intake = st.number_input(
        "Water Intake (Liters)",
        min_value=0.0,
        max_value=10.0,
        step=0.1
    )

    exercise_minutes = st.number_input(
        "Exercise Minutes",
        min_value=0,
        max_value=300,
        step=5
    )

    stress_level = st.slider(
        "Stress Level",
        1,
        10
    )

    symptoms = st.text_area("Symptoms")

    st.markdown("---")

    st.subheader("🌸 PCOS Risk Assessment")

    irregular_periods = st.selectbox(
        "Do you have Irregular Periods?",
        ["No", "Yes"]
    )

    acne = st.selectbox(
        "Do you frequently experience Acne?",
        ["No", "Yes"]
    )

    hair_loss = st.selectbox(
        "Do you experience Hair Loss?",
        ["No", "Yes"]
    )

    weight_gain = st.selectbox(
        "Recent Weight Gain?",
        ["No", "Yes"]
    )

    mood_swings = st.selectbox(
        "Mood Swings?",
        ["No", "Yes"]
    )

with right:

    st.info("""
### 🌸 Wellness Tips

💧 Drink 2-3 Liters Water

😴 Sleep 7-8 Hours

🏃 Exercise Daily

🧘 Reduce Stress

🥗 Healthy Nutrition
""")

    st.success("""
### 💜 Prevention Tips

Monitor symptoms

Track lifestyle habits

Stay active

Maintain healthy weight
""")

# -----------------------------
# ANALYZE BUTTON
# -----------------------------

if st.button("💜 Analyze Health", use_container_width=True):

    if "username" not in st.session_state:

        st.warning(
            "Please login first."
        )

        st.stop()

    username = st.session_state["username"]

    health_score = calculate_health_score(
        sleep_hours,
        water_intake,
        exercise_minutes,
        stress_level
    )

    pcos_risk = predict_pcos(
        irregular_periods,
        acne,
        hair_loss,
        weight_gain,
        mood_swings
    )

    recommendations = get_recommendations(
        health_score,
        pcos_risk
    )

    try:

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        name = st.session_state["username"]


        cursor.execute(
            """
            INSERT INTO health_logs
            (
                username,
                sleep_hours,
                water_intake,
                exercise_minutes,
                stress_level,
                symptoms,
                health_score,
                pcos_risk
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                username,
                sleep_hours,
                water_intake,
                exercise_minutes,
                stress_level,
                symptoms,
                health_score,
                pcos_risk
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Health Data Saved Successfully ✅"
        )

        st.markdown("---")

        st.subheader("📊 Assessment Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "💜 Health Score",
                f"{health_score}/100"
            )

        with col2:
            st.metric(
                "🌸 PCOS Risk",
                pcos_risk
            )

        if health_score >= 80:

            st.success(
                "Health Status: Excellent ✅"
            )

        elif health_score >= 60:

            st.info(
                "Health Status: Good 👍"
            )

        else:

            st.warning(
                "Health Status: Needs Attention ⚠️"
            )

        st.markdown("---")

        st.subheader(
            "💡 Personalized Recommendations"
        )

        for rec in recommendations:

            st.write(
                "✅",
                rec
            )

    except Exception as e:

        st.error(
            f"Database Error: {e}"
        )