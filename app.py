import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", layout="wide")

# ثيم أبيض نظيف
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; }
    h1 { color: #0f172a !important; text-align: center; }
    h3 { color: #1e293b !important; }
</style>
""", unsafe_allow_html=True)

st.title("✈️ احمد الدوسري للسفر والسياحة")
st.subheader("نظام إدارة حجوزات السفر")

# تهيئة البيانات
if 'bookings' not in st.session_state:
    st.session_state.bookings = []

with st.sidebar:
    st.header("بيانات الحجز")
    name = st.text_input("اسم العميل")
    dest = st.selectbox("الوجهة", ["الرياض", "جدة", "دبي", "القاهرة", "لندن", "اسطنبول"])
    travel_date = st.date_input("تاريخ الرحلة", value=date.today())
    if st.button("تأكيد الحجز", type="primary"):
        if name:
            st.session_state.bookings.append({"الاسم": name, "الوجهة": dest, "التاريخ": str(travel_date)})
            st.success(f"تم الحجز بنجاح للعميل {name}")
        else:
            st.warning("الرجاء ادخال اسم العميل")

st.write("### قائمة الحجوزات الحالية")
if st.session_state.bookings:
    df = pd.DataFrame(st.session_state.bookings)
    st.dataframe(df, use_container_width=True)
else:
    st.info("لا يوجد حجوزات حالياً")
