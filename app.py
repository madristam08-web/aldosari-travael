import streamlit as st
from datetime import date, datetime
import random

st.set_page_config(page_title="احمد الدوسري للسفر والسياحة", layout="wide")

# ===== بيانات حسابك - عدلها هنا صخ =====
BANK_NAME = "مصرف الراجحي"
ACCOUNT_NAME = "احمد الدوسري للسفر والسياحة"
IBAN = "SA38 8000 0000 6080 1016 7520"
ACCOUNT_NO = "608010167520"

st.markdown("""
<style>
.stApp { background-color: #f5f7fa !important; }
.header{ background: linear-gradient(135deg, #065f46 0%, #10b981 100%); padding:35px; border-radius:20px; text-align:center; color:white; margin-bottom:20px; }
.bank-box{ background:#fffbeb; border:2px dashed #d97706; border-radius:15px; padding:20px; margin:15px 0; }
</style>
<div class="header">
<h1 style='color:white !important;'>✈️ احمد الدوسري للسفر والسياحة</h1>
<p style='color:white !important;'>نظام إدارة الحجوزات الذكي</p>
</div>
""", unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: from_city = st.selectbox("من:", ["الرياض - RUH", "جدة - JED", "الدمام - DMM", "القصيم - ELQ"])
with c2: to_city = st.selectbox("إلى:", ["لندن - LHR", "دبي - DXB", "القاهرة - CAI", "اسطنبول - IST"])
with c3: travel_date = st.date_input("تاريخ السفر:", date.today())
with c4: passengers = st.number_input("المسافرين:", 1, 10, 1)

if st.button("✈️ بحث عن الرحلات", use_container_width=True, type="primary"):
    st.session_state['searched'] = True

if st.session_state.get('searched'):
    flights = [
        {"flight": "SV 110", "time": "08:30 - 12:45", "price": 1250},
        {"flight": "SV 102", "time": "14:20 - 18:35", "price": 1890},
        {"flight": "SV 118", "time": "22:10 - 02:30", "price": 1450},
    ]
    for f in flights:
        with st.container(border=True):
            a,b,c,d = st.columns([2,2,1,1])
            a.write(f"*{f['flight']}* - {f['time']}")
            b.write(f"{from_city} → {to_city} - {travel_date}")
            c.write(f"*{f['price']} ر.س*")
            if d.button("احجز", key=f['flight'], type="primary"):
                st.session_state['selected'] = f
                st.session_state['show_pay'] = True
                st.session_state['confirmed'] = False
                st.rerun()

if st.session_state.get('show_pay'):
    f = st.session_state['selected']
    with st.container(border=True):
        st.subheader(f"💳 إتمام حجز {f['flight']} - {f['price']} ر.س")
        pay = st.selectbox("اختر طريقة الدفع:", ["مدى - Mada", "Visa", "Mastercard", "Apple Pay", "STC Pay", "Tabby", "تحويل بنكي - الراجحي"])

        if pay == "تحويل بنكي - الراجحي":
            st.markdown(f"""
            <div class='bank-box'>
            <h3>🏦 بيانات التحويل البنكي - الراجحي</h3>
            <p>البنك: <b>{BANK_NAME}</b><br>
            اسم الحساب: <b>{ACCOUNT_NAME}</b><br>
            رقم الحساب: <b style='font-size:22px; color:#065f46;'>{ACCOUNT_NO}</b><br>
            الآيبان: <b style='font-size:18px; background:yellow; padding:3px 8px;'>{IBAN}</b></p>
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
            st.info(f"🧾 فاتورة: {f['flight']} | {from_city} → {to_city} | {travel_date} | {f['price']} ر.س | الدفع: {pay}")
            
            ticket_text = f"تذكرة احمد الدوسري\nرقم الحجز: {booking_no}\nالرحلة: {f['flight']}\nمن: {from_city} الى: {to_city}\nالتاريخ: {travel_date}\nالمبلغ: {f['price']} ر.س\nالدفع: {pay}\nالايبان: {IBAN}"
            st.download_button("🖨️ طباعة / تحميل التذكرة", ticket_text, file_name=f"{booking_no}.txt", use_container_width=True)
            st.warning(f"📲 ارسل رقم الحجز {booking_no} على الواتساب")
