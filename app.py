import streamlit as st, pandas as pd, requests
from datetime import date

st.set_page_config(page_title="احمد الدوسري", layout="wide")
st.image("https://upload.wikimedia.org/wikipedia/commons/0/0d/Saudi_Arabian_Airlines_Logo.png", width=180)
st.markdown("""
<style>
.header{background:linear-gradient(rgba(0,0,0,.6),rgba(0,0,0,.6)),url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05');background-size:cover;padding:60px;border-radius:20px;text-align:center;color:white}
</style>
<div class=header><h1 style='color:white'>✈️ احمد الدوسري للسفر والسياحة</h1><p>نظام الحجوزات الذكي</p></div>
""", unsafe_allow_html=True)

def get_temp(lat,lon):
    try:
        r=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true",timeout=4).json()
        return f"{r['current_weather']['temperature']}°C"
    except:
        return "28°C"

c1,c2,c3,c4=st.columns(4)
c1.metric("الرياض",get_temp(24.71,46.67),"☀️")
c2.metric("جدة",get_temp(21.54,39.17),"🌤️")
c3.metric("دبي",get_temp(25.20,55.27),"🔥")
c4.metric("لندن",get_temp(51.5,-0.12),"☁️")

st.write("### 🗺️ وجهاتنا")
st.map(pd.DataFrame({'lat':[24.71,21.54,25.20,51.5],'lon':[46.67,39.17,55.27,-0.12]}))

if 'bookings' not in st.session_state:
    st.session_state.bookings=[]

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/0d/Saudi_Arabian_Airlines_Logo.png",width=150)
    st.header("حجز جديد")
    name=st.text_input("اسم العميل")
    dest=st.selectbox("الوجهة",["الرياض","جدة","دبي","القاهرة","لندن","اسطنبول"])
    d=st.date_input("التاريخ",value=date.today())
    price={"الرياض":450,"جدة":600,"دبي":1200,"القاهرة":900,"لندن":2500,"اسطنبول":1800}
    st.info(f"السعر: {price[dest]} ريال")
    if st.button("تأكيد الحجز ✈️",type="primary",use_container_width=True):
        if name:
            st.session_state.bookings.append({"الاسم":name,"الوجهة":dest,"التاريخ":str(d),"السعر":price[dest]})
            st.success("تم الحجز!")
            st.balloons()

st.write("### 📋 الحجوزات")
if st.session_state.bookings:
    st.dataframe(pd.DataFrame(st.session_state.bookings),use_container_width=True)
else:
    st.info("لا يوجد حجوزات")
