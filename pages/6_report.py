import streamlit as st
import sqlite3
import pandas as pd

from datetime import datetime
from theme import load_css

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Health Report",
    page_icon="📄",
    layout="wide"
)

load_css()

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
<h1>📄 FemCare Health Report Center</h1>
<p>Generate and download personalized wellness reports</p>
</div>
""", unsafe_allow_html=True)

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
# LOAD USER DATA
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
    # USER SUMMARY
    # -----------------------------

    st.subheader("👤 Patient Details")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Username",
            username
        )

    with c2:
        st.metric(
            "Health Score",
            latest["health_score"]
        )

    with c3:
        st.metric(
            "PCOS Risk",
            latest["pcos_risk"]
        )

    st.markdown("---")

    # -----------------------------
    # BMI / HEALTH STATUS
    # -----------------------------

    st.subheader("💜 Health Status")

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
    # LATEST ASSESSMENT
    # -----------------------------

    st.subheader("📊 Latest Assessment")

    st.write(
        f"😴 Sleep Hours : {latest['sleep_hours']}"
    )

    st.write(
        f"💧 Water Intake : {latest['water_intake']} Liters"
    )

    st.write(
        f"🏃 Exercise Minutes : {latest['exercise_minutes']}"
    )

    st.write(
        f"🧘 Stress Level : {latest['stress_level']}"
    )

    st.write(
        f"🌸 PCOS Risk : {latest['pcos_risk']}"
    )

    st.write(
        f"📝 Symptoms : {latest['symptoms']}"
    )

    st.markdown("---")

    # -----------------------------
    # RECOMMENDATIONS
    # -----------------------------

    st.subheader("💡 Personalized Recommendations")

    recommendations = []

    if latest["water_intake"] < 2:
        recommendations.append(
            "Increase daily water intake."
        )

    if latest["sleep_hours"] < 7:
        recommendations.append(
            "Sleep at least 7-8 hours daily."
        )

    if latest["exercise_minutes"] < 30:
        recommendations.append(
            "Exercise regularly."
        )

    if latest["stress_level"] > 6:
        recommendations.append(
            "Practice stress management techniques."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "Maintain your healthy lifestyle."
        )

    for rec in recommendations:

        st.write(
            "✅",
            rec
        )

    st.markdown("---")

    # -----------------------------
    # REPORT GENERATION
    # -----------------------------

    if st.button(
        "📄 Generate Health Report",
        use_container_width=True
    ):

        pdf_file = "FemCare_Report.pdf"

        doc = SimpleDocTemplate(
            pdf_file
        )

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "FemCare AI Health Report",
                styles["Title"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

        content.append(
            Paragraph(
                f"Username: {username}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Health Score: {latest['health_score']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"PCOS Risk: {latest['pcos_risk']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Sleep Hours: {latest['sleep_hours']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Water Intake: {latest['water_intake']} Liters",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Exercise Minutes: {latest['exercise_minutes']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Stress Level: {latest['stress_level']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Symptoms: {latest['symptoms']}",
                styles["Normal"]
            )
        )

        content.append(
            Spacer(1, 15)
        )

        content.append(
            Paragraph(
                "Recommendations",
                styles["Heading2"]
            )
        )

        for rec in recommendations:

            content.append(
                Paragraph(
                    f"• {rec}",
                    styles["Normal"]
                )
            )

        content.append(
            Spacer(1, 15)
        )

        content.append(
            Paragraph(
                f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
                styles["Normal"]
            )
        )

        doc.build(content)

        st.success(
            "Health Report Generated Successfully ✅"
        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(
                label="⬇ Download PDF Report",
                data=file,
                file_name="FemCare_Report.pdf",
                mime="application/pdf"
            )

except Exception as e:

    st.error(
        f"Error: {e}"
    )