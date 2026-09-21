import streamlit as st
import pandas as pd
from datetime import date
import requests

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", layout="wide")

st.markdown("""
<style>
    .header {
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05');
        background-size: cover;
        background-position: center;
        padding: 70px 20px;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 15px;
    }
    .header h1 { color: white !important; font-size: 45px; margin-bottom:10px; }
    .news-ticker {
        background: #065f46;
        color: white;
        padding: 12px;
        border-radius: 10px;
        font-weight: bold;
    }
</style>
<div class="header">
    <h1>✈️ احمد الدوسري للسفر والسياحة</h1>
    <p style="font-size:22px;">نظام إدارة الحجوزات الذكي - معتمد من هيئة الطيران</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="news-ticker">
✈️ SAUDIA: رحلات مباشرة جديدة الرياض - لندن | 🌤️ أجواء مثالية للسفر هذا الأسبوع | 🛫 مطار الملك خالد: 100 ألف مسافر يومياً | 💚 عروض اليوم الوطني 95
</div>
""", unsafe_allow_html=True)

# طقس
st.write("### 🌤️ حالة الطقس الحي في وجهاتنا")
c1, c2, c3, c4 = st.columns(4)

def get_weather(lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        r = requests.get(url, timeout=5).json()
        return f"{r['current_weather']['temperature']}°C"
    except:
        return "28°C"

with c1: st.metric("🇸🇦 الرياض", get_weather(24.71, 46.67), "مشمس ☀️")
with c2: st.metric("🇸🇦 جدة", get_weather(21.54, 39.17), "معتدل 🌤️")
with c3: st.metric("🇦🇪 دبي", get_weather(25.20, 55.27), "حار 🔥")
with c4: st.metric("🇬🇧 لندن", get_weather(51.50, -0.12), "غائم ☁️")

# خريطة الرحلات
st.write("### 🗺️ خريطة وجهاتنا الرئيسية")
map_data = pd.DataFrame({
    'lat': [24.71, 21.54, 25.20, 41.00, 51.50, 30.04],
    'lon': [46.67, 39.17, 55.27, 28.97, -0.12, 31.23],
    'city': ['الرياض', 'جدة', 'دبي', 'اسطنبول', 'لندن', 'القاهرة']
})
st.map(map_data, zoom=2)
st.caption("نقاط وجهات السفر - اضغط تكبير للخريطة")

# الحجوزات
if 'bookings' not in st.session_state:
    st.session_state.bookings = []

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/0d/Saudi_Arabian_Airlines_Logo.png", width=200)
    st.header("📝 حجز جديد")
    name = st.text_input("اسم العميل")
    dest = st.selectbox("الوجهة", ["الرياض", "جدة", "دبي", "القاهرة", "لندن",
