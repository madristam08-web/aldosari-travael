import streamlit as st
import pandas as pd

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", page_icon="✈️", layout="wide")

st.title("✈️ احمد الدوسري للسفر والسياحة")
st.markdown("### نظام إدارة حجوزات السفر")

with st.sidebar:
    st.header("بيانات الحجز")
    name = st.text_input("اسم العميل")
    dest = st.selectbox("الوجهة", ["الرياض", "جدة", "دبي", "القاهرة", "لندن", "اسطنبول"])
    date = st.date_input("تاريخ الرحلة")

if st.button("تأكيد الحجز"):
    if name:
        df = pd.DataFrame([[name, dest, str(date)]], columns=["الاسم", "الوجهة", "التاريخ"])
        st.success(f"تم الحجز بنجاح للعميل {name}")
        st.dataframe(df)
    else:
        st.error("الرجاء إدخال الاسم")
