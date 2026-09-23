import streamlit as st
from datetime import date, datetime
import random

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", layout="wide")

BANK_NAME = "مصرف الراجحي"
ACCOUNT_NAME = "احمد الدوسري للسفر والسياحة"
IBAN = "SA38 8000 0000 6080 1016 7520"
ACCOUNT_NO = "608010167520"

# كل المطارات السعودية + العالمية
SAUDI_CITIES = ["الرياض - RUH", "جدة - JED", "الدمام - DMM", "القصيم - ELQ", "أبها - AHB", "تبوك - TUU", "المدينة - MED", "الطائف - TIF", "جيزان - GIZ", "حائل - HAS"]
WORLD_CITIES = ["دبي - DXB", "القاهرة - CAI", "لندن - LHR", "اسطنبول - IST", "الدوحة - DOH", "الكويت - KWI", "البحرين - BAH", "مسقط - MCT", "باريس - CDG", "نيويورك - JFK", "بانكوك - BKK", "كوالالمبور - KUL", "القاهرة - CAI", "عمان - AMM"]

st.title("✈️ احمد الدوسري للسفر والسياحة")
st.markdown("### اختر أي مدينة تبي - النظام يجيب لك رحلاتها فوراً")

c1,c2,c3,c4 = st.columns(4)
with c1: from_city = st.selectbox("من:", SAUDI_CITIES + WORLD_CITIES, index=0)
with c2: to_city = st.selectbox("إلى:", WORLD_CITIES + SAUDI_CITIES, index=0)
with c3: travel_date = st.date_input("تاريخ السفر:", date.today())
with c4: passengers = st.number_input("المسافرين:", 1, 10, 1)

if st.button("✈️ بحث عن الرحلات", use_container_width=True, type="primary"):
    if from_city == to_city:
        st.error("⚠️ لا يمكن السفر من نفس المدينة إلى نفسها!")
    else:
        st.session_state['searched'] = True
        st.session_state['from'] = from_city
        st.session_state['to'] = to_city
        # سعر يتغير حسب المسافة
        base_price = 800 if "DXB" in to_city or "DOH" in to_city or "KWI" in to_city else 1800
        st.session_state['base_price'] = base_price

if st.session_state.get('searched'):
    from_city = st.session_state['from']
    to_city = st.session_state['to']
    base = st.session_state['base_price']
    
    st.subheader(f"🎫 الرحلات من {from_city} إلى {to_city}")
    flights = [
        {"flight": f"SV {random.randint(100,999)}", "time": "08:30 - 12:45", "price": base + random.randint(0,200)},
        {"flight": f"SV {random.randint(100,999)}", "time": "14:20 - 18:35", "price": base + random.randint(300,600)},
        {"flight": f"SV {random.randint(100,999)}", "time": "22:10 - 02:30", "price": base + random.randint(100,400)},
    ]
    for f in flights:
        with st.container(border=True):
            a,b,c,d = st.columns([2,2,1,1])
            a.write(f"*{f['flight']}* - {f['time']}")
            b.write(f"{from_city} → {to_city}")
            c.write(f"*{f['price']} ر.س*")
            if d.button("احجز", key=f['flight'], type="primary"):
                st.session_state['selected'] = f
                st.session_state['show_pay'] = True
                st.session_state['confirmed'] = False
                st.rerun()

if st.session_state.get('show_pay'):
    f = st.session_state['selected']
    with st.container(border=True):
        st.subheader(f"💳 اتمام حجز {f['flight']} - {f['price']} ر.س")
        st.write(f"المسار: {st.session_state['from']} → {st.session_state['to']}")
        pay = st.selectbox("اختر طريقة الدفع:", ["تحويل بنكي - الراجحي", "مدى - Mada", "Visa", "Mastercard", "Apple Pay", "STC Pay", "Tabby"])

        st.markdown(f"""
        <div style='background:#fffbeb; border:2px dashed #d97706; border-radius:15px; padding:15px;'>
        🏦 <b>حساب التاجر:</b> {ACCOUNT_NAME}<br>
        رقم الحساب: <b>{ACCOUNT_NO}</b><br>
        الآيبان: <b style='background:yellow'>{IBAN}</b>
        </div>
        """, unsafe_allow_html=True)

        if st.button("💚 تأكيد الحجز وطباعة التذكرة", use_container_width=True, type="primary"):
            booking_no = f"AHM-{random.randint(10000,99999)}"
            st.session_state['booking_no'] = booking_no
            st.session_state['confirmed'] = True
            st.balloons()
            st.rerun()

        if st.session_state.get('confirmed'):
            booking_no = st.session_state['booking_no']
            st.success(f"✅ تم الحجز بنجاح! رقم حجزك: {booking_no}")
            ticket_text = f"تذكرة احمد الدوسري\nالحجز: {booking_no}\nمن: {st.session_state['from']} الى: {st.session_state['to']}\nالتاريخ: {travel_date}\nالرحلة: {f['flight']}\nالسعر: {f['price']}\nحساب التاجر: {ACCOUNT_NO}\nIBAN: {IBAN}"
            st.download_button("🖨️ طباعة التذكرة", ticket_text, file_name=f"{booking_no}.txt", use_container_width=True)
