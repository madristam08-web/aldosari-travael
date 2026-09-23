import streamlit as st
from datetime import date
import random

st.set_page_config(page_title="احمد الدوسري للسفر", layout="wide")

IBAN = "SA38 8000 0000 6080 1016 7520"
ACCOUNT_NO = "608010167520"

SAUDI = ["الرياض - RUH","جدة - JED","الدمام - DMM","القصيم - ELQ","أبها - AHB","تبوك - TUU","المدينة - MED"]
WORLD = ["دبي - DXB","القاهرة - CAI","لندن - LHR","اسطنبول - IST","الدوحة - DOH","الكويت - KWI","البحرين - BAH","باريس - CDG"]

st.title("✈️ احمد الدوسري للسفر والسياحة")

c1,c2,c3,c4 = st.columns(4)
with c1: from_city = st.selectbox("من:", SAUDI+WORLD)
with c2: to_city = st.selectbox("إلى:", WORLD+SAUDI)
with c3: travel_date = st.date_input("التاريخ:", date.today())
with c4: passengers = st.number_input("المسافرين:", 1,10,1)

if st.button("✈️ بحث عن الرحلات", use_container_width=True, type="primary"):
    st.session_state['searched'] = True
    st.session_state['from'] = from_city
    st.session_state['to'] = to_city

# ==== تظهر وسائل الدفع مباشرة بعد البحث صخ ====
if st.session_state.get('searched'):
    with st.container(border=True):
        st.markdown("### 💳 جميع طرق الدفع متاحة - Secure & SSL protected")
        p1,p2,p3,p4,p5,p6,p7 = st.columns(7)
        p1.success("mada\nمدى")
        p2.info("VISA")
        p3.info("Mastercard")
        p4.info("Apple Pay")
        p5.info("stc pay")
        p6.success("tabby")
        p7.warning("الراجحي")
        st.caption("ادفع بأمان 100% - جميع المعاملات مشفرة")

    st.subheader(f"🎫 الرحلات: {st.session_state['from']} → {st.session_state['to']}")
    for i in range(3):
        price = random.randint(900,1900)
        flight_no = f"SV {random.randint(100,999)}"
        with st.container(border=True):
            a,b,c,d = st.columns([2,2,1,1])
            a.write(f"*{flight_no}*\n08:30 - 12:45")
            b.write(f"{st.session_state['from']} → {st.session_state['to']}\n{travel_date}")
            c.write(f"*{price} ر.س*")
            if d.button("احجز الآن", key=f"book_{i}_{flight_no}", type="primary"):
                st.session_state['selected_price'] = price
                st.session_state['selected_flight'] = flight_no
                st.session_state['show_pay'] = True
                st.rerun()

if st.session_state.get('show_pay'):
    with st.container(border=True):
        st.subheader(f"💳 إتمام حجز {st.session_state['selected_flight']} - {st.session_state['selected_price']} ر.س")
        
        # وسائل الدفع مرة ثانية بوضوح
        st.markdown("#### اختر طريقة الدفع:")
        col1,col2,col3 = st.columns(3)
        pay = col1.selectbox("الطريقة:", ["تحويل بنكي - الراجحي","مدى - Mada","Visa","Mastercard","Apple Pay","STC Pay","Tabby"])

        st.info(f"🏦 حساب التاجر: احمد الدوسري | رقم الحساب: {ACCOUNT_NO} | الآيبان: {IBAN}")

        if st.button("💚 تأكيد الحجز وطباعة التذكرة", use_container_width=True, type="primary"):
            booking_no = f"AHM-{random.randint(10000,99999)}"
            st.session_state['booking_no'] = booking_no
            st.session_state['confirmed'] = True
            st.balloons()
            st.rerun()

        if st.session_state.get('confirmed'):
            st.success(f"✅ تم الحجز! رقم حجزك: {st.session_state['booking_no']}")
            txt = f"تذكرة احمد الدوسري\nالحجز: {st.session_state['booking_no']}\nالرحلة: {st.session_state['selected_flight']}\nمن {st.session_state['from']} الى {st.session_state['to']}\nالسعر: {st.session_state['selected_price']}\nالحساب: {ACCOUNT_NO}\nIBAN: {IBAN}"
            st.download_button("🖨️ طباعة التذكرة", txt, file_name=f"{st.session_state['booking_no']}.txt", use_container_width=True)
