import streamlit as st

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="FemCare AI",
    page_icon="💜",
    layout="wide"
)

# --------------------------------
# HERO TITLE
# --------------------------------

st.markdown(
    """
    <h1 style='text-align:center;color:#C084FC;font-size:65px;'>
    💜 FemCare AI
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h3 style='text-align:center;color:white;'>
    Intelligent Women's Health Tracking and PCOS Risk Prediction Platform
    </h3>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------
# HERO BANNER
# --------------------------------

st.markdown(
    """
    <div style="
    padding:40px;
    border-radius:15px;
    background: linear-gradient(90deg,#7E22CE,#C084FC);
    text-align:center;
    color:white;
    ">

    <h1>💜 AI-Powered Women's Health Companion</h1>

    <h3>
    Track • Predict • Prevent
    </h3>

    <p>
    Monitor your daily health, assess PCOS risk,
    receive personalized recommendations,
    and visualize your wellness journey using AI.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------
# HEALTH JOURNEY
# --------------------------------

st.header("🌸 Your Health Journey")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    if st.button(
        "📝 Register",
        use_container_width=True
    ):
        st.switch_page(
            "pages/1_register.py"
        )

with col2:
    if st.button(
        "🔐 Login",
        use_container_width=True
    ):
        st.switch_page(
            "pages/2_login.py"
        )

with col3:
    if st.button(
        "👤 Profile",
        use_container_width=True
    ):
        st.switch_page(
            "pages/3_profile.py"
        )

with col4:
    if st.button(
        "💜 Assessment",
        use_container_width=True
    ):
        st.switch_page(
            "pages/4_Health_Assessment.py"
        )

with col5:
    if st.button(
        "📊 Dashboard",
        use_container_width=True
    ):
        st.switch_page(
            "pages/5_dashboard.py"
        )

with col6:
    if st.button(
        "📄 Report",
        use_container_width=True
    ):
        st.switch_page(
            "pages/6_report.py"
        )

st.markdown("---")
# --------------------------------
# FEATURES
# --------------------------------

st.header("🚀 Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(
        """
        🌸 PCOS Risk Assessment
        
        Predict PCOS risk levels using
        intelligent health analysis.
        """
    )

with col2:
    st.info(
        """
        💜 Daily Health Tracking
        
        Monitor sleep, water intake,
        exercise and stress.
        """
    )

with col3:
    st.info(
        """
        📊 Smart Analytics
        
        Visualize health insights
        through interactive dashboards.
        """
    )

st.markdown("---")

# --------------------------------
# WHY FEMCARE AI
# --------------------------------

st.header("💡 Why Choose FemCare AI?")

st.write("""
FemCare AI is a machine learning-based healthcare platform
designed specifically for women's wellness.

The platform helps users:

✅ Monitor daily health habits

✅ Assess PCOS risk

✅ Improve lifestyle awareness

✅ Generate personalized recommendations

✅ Visualize health analytics

✅ Download health reports

✅ Promote preventive healthcare practices
""")

st.markdown("---")

# --------------------------------
# PLATFORM HIGHLIGHTS
# --------------------------------

st.header("📈 Platform Highlights")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "ML Accuracy",
        "87.96%"
    )

with c2:
    st.metric(
        "Health Parameters",
        "5+"
    )

with c3:
    st.metric(
        "Core Modules",
        "6"
    )

with c4:
    st.metric(
        "Reports",
        "PDF"
    )

st.markdown("---")

# --------------------------------
# ABOUT PROJECT
# --------------------------------

st.header("👩‍⚕️ About FemCare AI")

st.write("""
FemCare AI is an intelligent healthcare platform developed
to support women in monitoring their health and identifying
potential PCOS risks at an early stage.

The platform combines machine learning, health analytics,
risk prediction, and personalized recommendations to
encourage healthier lifestyle decisions.
""")

st.markdown("---")

# --------------------------------
# GET STARTED
# --------------------------------

st.header("🚀 Get Started")

st.success(
    """
    Follow the steps from the sidebar:

    1️⃣ Register

    2️⃣ Login

    3️⃣ Complete Profile

    4️⃣ Health Assessment

    5️⃣ Dashboard

    6️⃣ Download Health Report
    """
)

st.info(
    "💜 Your Health Journey Starts Here!"
)
st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;color:gray;'>
    💜 FemCare AI | Final Year Project
    <br>
    Machine Learning Based Women's Health Monitoring Platform
    </div>
    """,
    unsafe_allow_html=True
)