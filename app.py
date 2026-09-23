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
# صخحت المفاتيح هنا - لا تستخدم from
with c1: from_city = st.selectbox("من:", SAUDI+WORLD, key="origin_key")
with c2: to_city = st.selectbox("إلى:", WORLD+SAUDI, key="dest_key")
with c3: travel_date = st.date_input("التاريخ:", date.today())
with c4: passengers = st.number_input("المسافرين:", 1,10,1)

if st.button("✈️ بحث عن الرحلات", use_container_width=True, type="primary"):
    if from_city == to_city:
        st.error("اختر مدن مختلفة")
    else:
        st.session_state['searched'] = True
        st.session_state['origin_city'] = from_city
        st.session_state['dest_city'] = to_city
        st.session_state['travel_date_val'] = str(travel_date)
        st.session_state['flights'] = [
            {"flight": f"SV {random.randint(100,999)}", "time": "08:30 - 12:45", "price": random.randint(900,1200)},
            {"flight": f"SV {random.randint(100,999)}", "time": "14:20 - 18:35", "price": random.randint(1300,1900)},
            {"flight": f"SV {random.randint(100,999)}", "time": "22:10 - 02:30", "price": random.randint(900,1500)},
        ]
        st.session_state['show_pay'] = False
        st.session_state['confirmed'] = False

if st.session_state.get('searched'):
    with st.container(border=True):
        st.markdown("### 💳 جميع طرق الدفع متاحة")
        p1,p2,p3,p4,p5,p6,p7 = st.columns(7)
        p1.success("مدى")
        p2.info("VISA")
        p3.info("Mastercard")
        p4.info("Apple Pay")
        p5.info("stc pay")
        p6.success("tabby")
        p7.warning("الراجحي")

    st.subheader(f"🎫 الرحلات: {st.session_state['origin_city']} → {st.session_state['dest_city']}")
    
    for i, f in enumerate(st.session_state['flights']):
        with st.container(border=True):
            a,b,c,d = st.columns([2,2,1,1])
            a.write(f"*{f['flight']}*\n{f['time']}")
            b.write(f"{st.session_state['origin_city']} → {st.session_state['dest_city']}\n{st.session_state['travel_date_val']}")
            c.write(f"*{f['price']} ر.س*")
            if d.button("احجز الآن", key=f"book_btn_{i}", type="primary", use_container_width=True):
                st.session_state['selected_price'] = f['price']
                st.session_state['selected_flight'] = f['flight']
                st.session_state['show_pay'] = True
                st.session_state['confirmed'] = False
                st.rerun()

if st.session_state.get('show_pay'):
    with st.container(border=True):
        st.subheader(f"💳 إتمام حجز {st.session_state['selected_flight']} - {st.session_state['selected_price']} ر.س")
        st.write(f"المسار: {st.session_state['origin_city']} → {st.session_state['dest_city']}")
        
        pay = st.selectbox("اختر طريقة الدفع:", ["تحويل بنكي - الراجحي","مدى - Mada","Visa","Mastercard","Apple Pay","STC Pay","Tabby"])
        
        st.warning(f"🏦 حساب التاجر: احمد الدوسري\nرقم الحساب: {ACCOUNT_NO}\nالآيبان: {IBAN}")

        if st.button("💚 تأكيد الحجز وطباعة التذكرة", use_container_width=True, type="primary"):
            booking_no = f"AHM-{random.randint(10000,99999)}"
            st.session_state['booking_no'] = booking_no
            st.session_state['confirmed'] = True
            st.balloons()
            st.rerun()

        if st.session_state.get('confirmed'):
            st.success(f"✅ تم الحجز! رقم حجزك: {st.session_state['booking_no']}")
            txt = f"تذكرة احمد الدوسري\nالحجز: {st.session_state['booking_no']}\nالرحلة: {st.session_state['selected_flight']}\nمن {st.session_state['origin_city']} الى {st.session_state['dest_city']}\nالسعر: {st.session_state['selected_price']} ر.س\nالحساب: {ACCOUNT_NO}\nIBAN: {IBAN}"
            st.download_button("🖨️ طباعة التذكرة", txt, file_name=f"{st.session_state['booking_no']}.txt", use_container_width=True)
