import streamlit as st
import pandas as pd
from datetime import date
import requests

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", layout="wide")

# --- خلفية طيران + تصميم فخم ---
st.markdown("""
<style>
    .header {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05');
        background-size: cover;
        background-position: center;
        padding: 60px 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    .header h1 { color: white !important; font-size: 42px; }
    .weather-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
    }
    .news-ticker {
        background: #0f172a;
        color: white;
        padding: 10px;
        border-radius: 8px;
        overflow: hidden;
        white-space: nowrap;
    }
</style>
<div class="header">
    <h1>✈️ احمد الدوسري للسفر والسياحة</h1>
    <p style="font-size:20px;">نظام إدارة الحجوزات الذكي مع متابعة الطقس والطيران</p>
</div>
""", unsafe_allow_html=True)

# --- أخبار الطيران ---
st.markdown("""
<div class="news-ticker">
    ✈️ عاجل: الخطوط السعودية تعلن زيادة الرحلات لجدة ودبي | 🌤️ طقس مستقر في الرياض وجدة هذا الأسبوع | 🛫 مطار الملك خالد يستقبل 100 ألف مسافر يومياً | ✈️ عروض خاصة لرحلات لندن واسطنبول
</div>
""", unsafe_allow_html=True)

# --- الطقس الحي ---
st.write("### 🌤️ حالة الطقس في وجهاتنا")
col1, col2, col3 = st.columns(3)

def get_weather(city, lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        r = requests.get(url, timeout=5).json()
        temp = r['current_weather']['temperature']
        return f"{temp}°C"
    except:
        return "25°C"

with col1:
    st.metric("الرياض", get_weather("الرياض", 24.71, 46.67), "مشمس ☀️")
with col2:
    st.metric("جدة", get_weather("جدة", 21.54, 39.17), "معتدل 🌤️")
with col3:
    st.metric("دبي", get_weather("دبي", 25.20, 55.27), "حار 🔥")

# --- نظام الحجوزات ---
if 'bookings' not in st.session_state:
    st.session_state.bookings = []

with st.sidebar:
    st.header("📝 حجز جديد")
    name = st.text_input("اسم العميل")
    dest = st.selectbox("الوجهة", ["الرياض", "جدة", "دبي", "القاهرة", "لندن", "اسطنبول"])
    travel_date = st.date_input("تاريخ الرحلة", value=date.today())
    if st.button("تأكيد الحجز ✈️", type="primary"):
        if name:
            st.session_state.bookings.append({"الاسم": name, "الوجهة": dest, "التاريخ": str(travel_date)})
            st.success(f"تم الحجز بنجاح للعميل {name}")
        else:
            st.warning("الرجاء ادخال اسم العميل")

st.write("### 📋 قائمة الحجوزات")
if st.session_state.bookings:
    st.dataframe(pd.DataFrame(st.session_state.bookings), use_container_width=True)
else:
    st.info("لا يوجد حجوزات حالياً - ابدأ بإضافة حجز من القائمة الجانبية")
